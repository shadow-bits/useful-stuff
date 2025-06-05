# Calculate your WAM with a breeze

# TODO: Add Exception Handling

# Format of .txt file:
# <subjectcode>;<credit_pt>;<marks>     <-- semicolon cus easier to type
class Subject:
    def __init__ (self, subject_code, credit, mark):
        self._subject_code = subject_code
        self._credit = credit
        self._mark = mark

    def __str__ (self):
        out = f"Subject Code: {self._subject_code:<12}"
        out += f"Credits: {self._credit:<6}"
        out += f"Marks: {self._mark:<6}\t"
        return out
    
    def get_credit(self):
        return self._credit
    
    def get_mark(self):
        return self._mark

def read_file(filename):
    # stores list of subjects
    sub_li = []
    with open(filename, 'r') as file:
        for line in file:
            # SEMI-COLON FOR EZ TYPING
            subject_code, credit, mark = line.strip().split(';')
            try: 
                credit = int(credit)
                mark = int(mark)
            except ValueError:
                print("credit or mark not INT!")
            sub_li.append(Subject(subject_code, credit, mark))

    # Prints all processed inputs
    for s in sub_li:
        print(s)
    return sub_li

def calculate_wam(sub_li):
    total_credit = 0
    total_weighted_mark = 0
    
    for s in sub_li:
        total_credit += s.get_credit()
        total_weighted_mark += ( s.get_mark() * s.get_credit() )

    #print("credit: ", total_credit)
    #print("mark: :", total_weighted_mark)
    wam = total_weighted_mark / total_credit
    print(f"\nWAM: {wam:.2f}")

#====================================================

def main():
    filename = 'marks.txt'
    subject_list = read_file(filename)
    calculate_wam(subject_list)

if __name__ == "__main__":
    main()