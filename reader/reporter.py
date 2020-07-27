import time

# Number of seconds to wait between printing lines, to avoid spam.
MIN_REPORT_TIME = 1.0

class Reporter:
    def __init__(self, total, chunks=0, updates=100):
        """
        Set up the basis for the reporter.

        :param total: The total/max length of what we're reportin gon.
        :param chunks: Optional: Size of each chunk when we report.
        :param updates: Optioal: How many chunks to report (100 is an update for every percentage)
        """

        self.total = total
        if chunks > 0:
            self.chunks = chunks
        elif updates > 0:
            self.chunks = int(total / updates)
        else:
            raise Exception("You have to define chunks OR updates > 0.")
        self.start = time.time()
        self.last = self.start

    def report(self, current):
        """
        Report every X chunks.

        :param current: The current index.
        """
        if current % self.chunks == 0:
            # If the time since the last report is less than 1 second, skip it.
            cur_time = time.time()
            if cur_time - self.last < MIN_REPORT_TIME:
                return
            self.last = cur_time

            # Get progress percentage.
            percentage = round(current / self.total * 100, 1)
            # Get time passed.
            time_passed = round(cur_time - self.start, 2)
            print("... {:5}% - {}s".format(percentage, time_passed))
