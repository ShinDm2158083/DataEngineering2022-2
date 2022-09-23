#202158083 과제2

#네 과목과 각 과목의 점수 리스트로 저장
subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]

#위의 두 리스트를 이차원 리스트 형태로 전환
gradebook=[[0 for i in range(2)]for j in range(4)]

for i in range(4):
    gradebook[i][0] = subjects[i]
    gradebook[i][1] = grades[i]

print(gradebook)

#computer science과목과 점수를 .append()로 추가
gradebook.append(["computer science",100])
#visual arts과목과 점수를 append로 추가
gradebook.append(["viusal arts",93])
print(gradebook)

gradebook[5][1]+=5          #visual arts의 점수를 5증가된 점수로 수정
gradebook[2].remove(85)     #poety 점수를 삭제
gradebook[2].append('pass') #poety의 점수 방식을 Pass/Fail로 변경
print(gradebook)

#막학기 gradebook을 저장하고, full_gradebook에 두 gradebook을 더해 저장
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)