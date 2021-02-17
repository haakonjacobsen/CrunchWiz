class PreProcessor:
    def process(self, src_path, lines):
        if "wristband" in src_path:
            lines = [line.rstrip('\n') for line in lines]
            return "wristband", "EDA", lines
        elif "motion" in src_path:
            lines = [line.rstrip('\n') for line in lines]
            return "motion", "skeletal data", lines
        elif "eye" in src_path:
            lines = [line.rstrip('\n') for line in lines]
            return "eye tracker", "pupil", lines
