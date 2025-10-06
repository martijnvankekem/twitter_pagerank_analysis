import time


class Analysis:
    def __init__(self, id: str, description: str):
        self.start_time = None
        self.end_time = None
        self.iteration_start_time = None
        self.iterations = []
        self.id = id
        self.name = description

    def start(self):
        """
        Start the analysis.
        """
        self.start_time = time.time_ns()

    def start_iteration(self):
        """
        Log that an iteration has started.
        """
        self.iteration_start_time = time.time_ns()

    def stop_iteration(self):
        """
        Log that an iteration has finished.
        """
        if self.iteration_start_time is None:
            return

        # Save duration and reset start timer.
        self.iterations.append(time.time_ns() - self.iteration_start_time)
        self.iteration_start_time = None

    def stop(self):
        """
        Stop the analysis.
        """
        self.end_time = time.time_ns()

    def __str__(self):
        """
        String representation of the object, used for printing.
        """
        result = "Run-time and complexity analysis\n"
        result += "-- id: " + self.id + "\n"
        result += "-- name: " + self.name + "\n"
        if self.end_time is not None:
            duration = self.end_time - self.start_time
            result += "-- duration: {} ms ({} ns)\n".format(duration // 1_000_000, duration)
            result += "   > start time (in ns): " + str(self.start_time) + "\n"
            result += "   > end time (in ns): " + str(self.end_time) + "\n"
        else:
            result += "-- duration: not yet stopped\n"
            result += "   > start time (in ns): " + str(self.start_time) + "\n"

        result += "-- iterations: {}".format(len(self.iterations)) + "\n"
        if len(self.iterations) > 0:
            # Get average per iteration
            avg = sum(self.iterations) / len(self.iterations)
            avg_ms = avg // 1_000_000
            result += ("   > avg. duration per iteration: {} ms ({} ns)"
                       .format(avg_ms, avg) + "\n")

            # Write individual iterations
            for index, iteration in enumerate(self.iterations):
                in_ms = iteration // 1_000_000
                value = "{} ms ({} ns)".format(in_ms, iteration)
                result += "   > iteration " + str(index) + ": " + value + "\n"

        return result

    def write_to_file(self, out_path: str):
        """
        Write the analysis to a file.

        Parameters
        ----------
        out_path: the output location.
        """
        with open("output/" + out_path + "/analysis/{}.txt".format(self.id), "w") as f:
            f.write(str(self) + "\n\n")