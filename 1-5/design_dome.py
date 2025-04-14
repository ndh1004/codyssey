import numpy as np

def readCSV(filename):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[1:]:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        strength = float(parts[1])
                        data.append([strength])
                    except ValueError:
                        continue
    except Exception as e:
        print(f'파일 읽기 오류: {e}')
    return np.array(data)

# 각 CSV 파일 읽기
arr1 = readCSV('mars_base_main_parts-001.csv')
arr2 = readCSV('mars_base_main_parts-002.csv')
arr3 = readCSV('mars_base_main_parts-003.csv')

# 배열 합치기
parts = np.vstack((arr1, arr2, arr3))

# 평균값 계산
parts_mean = np.mean(parts, axis=1)

# 평균값 < 50 추출
parts_to_work_on = parts[parts_mean < 50]

# parts_to_work_on.csv 만들어 저장
try:
    np.savetxt('parts_to_work_on.csv', parts_to_work_on, delimiter=',', fmt='%.2f')
except Exception as e:
    print('파일 저장 오류:', e)

#전치행렬
try:
    parts2 = np.loadtxt('parts_to_work_on.csv', delimiter=',')
    parts3 = parts2.T
    print('전치 행렬 :')
    print(parts3)
except Exception as e:
    print(e)
