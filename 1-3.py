# csv 파일 읽기
try:
    with open('Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
except (FileNotFoundError, Exception) as e:
    print(f"에러 : {str(e)}")
    exit()

print('csv 파일 출력:')
for line in lines:
    print(line.strip())

# 데이터 처리
if not lines:
    print("파일이 없습니다.")
    exit()

header = lines[0].strip().split(',')
data = [line.strip().split(',') for line in lines[1:]]

# 인화성 기준 정렬 (내림차순)
try:
    sorted_data = sorted(data, key=lambda x: float(x[4]), reverse=True)
except (IndexError, ValueError) as e:
    print(f"에러 : {str(e)}")
    exit()

# 위험 물질 필터링 (0.7 이상)
high_flammability = [row for row in sorted_data if float(row[4]) >= 0.7]

print('\n인화성 물질 0.7 이상 목록 : ')
for row in high_flammability:
    print(','.join(row))

# 위험 물질 csv 저장
try:
    with open('Mars_Base_Inventory_danger.csv', 'w', encoding='utf-8') as f:
        f.write(','.join(header) + '\n')
        for row in high_flammability:
            f.write(','.join(row) + '\n')
except Exception as e:
    print(f"저장 중 에러 : {str(e)}")

try:
    with open('Mars_Base_Inventory_List.bin', 'wb') as f:   #이진파일 쓰기
        for row in [header] + sorted_data:
            f.write(','.join(row).encode('utf-8') + b'\n')

    # 이진파일 읽기 및 출력
    with open('Mars_Base_Inventory_List.bin', 'rb') as f:   #이진파일 읽기
        content = f.read().decode('utf-8')
        print('\n이진파일 :')
        print(content)
except Exception as e:
    print(f"이진파일 에러 : {str(e)}")

### 텍스트 vs 이진파일 차이점
#[텍스트 파일]
#장점: 텍스트 편집기로 수정 가능, 사람이 읽을 수 있음, 간단하고 이동이 쉽다.
#단점: 대용량 처리 비효율적, 이진 파일에 비해 속도가 느리고, 정밀도 또한 유지하기 어렵다.

#[이진 파일]
#장점: 저장 공간 효율적, 텍스트 파일에 비해 속도가 빠르며, 정밀도 또한 정확하게 유지가 가능하다
#단점: 직접 내용 확인 불가능, 사람이 읽을 수 없고, 복잡하고 이동이 어려움
