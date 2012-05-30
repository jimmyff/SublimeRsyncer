import sublime
import sublime_plugin
import subprocess
import threading
import sys


class SublimeRsyncer(sublime_plugin.EventListener):
    def on_post_save(self, view):
        settings = sublime.load_settings('SublimeRsyncer.sublime-settings')
        folders = settings.get("folders")
        current_file = view.file_name()
        if folders:
            for folder in folders:
                if current_file[:len(folder['localPath'])] == folder['localPath']:

                    # spawn a thread so non-blocking
                    thread = Rsync(folder['localPath'], folder['remote'], folder['exclude'], folder['deleteAfter'])
                    thread.start()


class Rsync(threading.Thread):
    def __init__(self, localPath, remote, exclude, deleteAfter):
        self.localPath = localPath
        self.remote = remote
        self.exclude = exclude
        self.deleteAfter = deleteAfter
        self.result = None
        threading.Thread.__init__(self)

    def run(self):

        commandComponents = ['rsync', '-avz', self.localPath, self.remote]

        if self.deleteAfter:
            commandComponents.insert(2, "--delete-after")

        if self.exclude:
            for excludeItem in self.exclude:
                commandComponents.insert(2, "--exclude="+excludeItem)

        sys.stdout.write('SublimeRsyncer command: '+' '.join(commandComponents)+'\n');
        sys.stdout.flush()

        process = subprocess.Popen(
            commandComponents,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        error = False

        while True:
            next_line = process.stdout.readline()
            if next_line == '' and process.poll() != None:
                break
            sys.stdout.write(next_line)
            sys.stdout.flush()

        while True:
            next_line = process.stderr.readline()
            if next_line == '' and process.poll() != None:
                break
            sys.stderr.write(next_line)
            sys.stderr.flush()
            error = True

        if (error == True):
            print "SublimeRsyncer: Failed! :-("
        else:
            print "SublimeRsyncer: Done :-)"

        return
