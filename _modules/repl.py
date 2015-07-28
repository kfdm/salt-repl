import sys
__salt__ = {}

def __virtual__():
    return True


def repl():

    class SaltREPL(cmd.Cmd):
        prompt = '<Salt> '

        def emptyline(self):
            pass

        def completedefault(text, line, begidx, endidx):
            return __salt__.keys()

        def default(self, line):
            if line == 'EOF':
                return False
            try:
                command, parts = line.split(' ', 1)
            except ValueError:
                command, parts = line, []

            print 'default', command, parts

        def do_help(self, arg):
            if arg:
                if arg in __salt__:
                    self.stdout.write('%s\n' % str(__salt__[arg].__doc__))
                else:
                    commands = []
                    for command in __salt__.keys():
                        if command.startswith(arg):
                            commands.append(command)

                    self.print_topics(self.doc_header, sorted(commands), 15, 80)
            else:
                self.stdout.write('%s\n' % str(self.doc_leader))
                self.print_topics(self.doc_header, sorted(__salt__.keys()), 15, 80)

    return SaltREPL().cmdloop()
    if sys.platform == 'darwin':
        SaltREPL('bind ^I rl_complete').cmdloop()
    else:
        SaltREPL('tab:complete').cmdloop()
