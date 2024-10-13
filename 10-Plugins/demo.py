from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'output'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.task_ok_count = 0
        self.task_failed_count = 0

    def v2_playbook_on_start(self, playbook):
        print("Starting playbook: {}".format(playbook._file_name))

    def v2_playbook_on_task_start(self, task, is_conditional):
        print("Starting task: {}".format(task.name))

    def v2_runner_on_ok(self, result):
        self.task_ok_count += 1
        print("Task succeeded on host: {}".format(result._host.name))

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.task_failed_count += 1
        print("Task failed on host: {}".format(result._host.name))

    def v2_playbook_on_stats(self, stats):
        print("Playbook completed")
        print("Tasks succeeded: {}".format(self.task_ok_count))
        print("Tasks failed: {}".format(self.task_failed_count))
