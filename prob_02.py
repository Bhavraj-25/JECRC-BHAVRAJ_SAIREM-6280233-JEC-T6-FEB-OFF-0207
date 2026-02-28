class Solution:

    def subject_average(self, students):
        subject_total = {}
        subject_count = {}
        ## Write your code here and don't forget to add return keyword
        for student in students:
            for sub, marks in student["marks"].items():
                if sub in subject_total:
                    subject_total[sub] += marks
                    subject_count[sub] += 1
                else:
                    subject_total[sub] = marks
                    subject_count[sub] = 1
        subject_average = {}
        for subj in subject_total:
            subject_average[subj] = subject_total[subj]/subject_count[subj]

        high_subj = None
        max_avg = 0

        for subject in subject_average:
            if subject_average[subject] > max_avg:
                max_avg = subject_average[subject]
                high_subj = subject

        return subject_average, high_subj