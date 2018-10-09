import time

class Main:
    def run(self, flink):
        env = flink.get_execution_environment()

        text = env \
            .from_collection(["Hello World"]) \
            .write_as_text("/app/out/helloworld_%f" % time.time())

        env.execute("Hello World example (py)")

"""
Prints Hello World into a timestamped file.
"""
def main(flink):
    Main().run(flink)
