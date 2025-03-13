#문제1 미션 컴퓨터를 복구하고 사고 원인을 파악해 보자

def read_log_file(filename):    #예외처리
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f'파일 {filename}을(를) 찾을 수 없습니다.')
    except PermissionError:
        print(f'파일 {filename}에 접근할 수 없습니다.')
    except TimeoutError:
        print(f'오류: {filename} 파일을 열 때 시간이 초과되었습니다.')
    except IsADirectoryError:
        print(f'오류: {filename} 경로가 디렉토리입니다. 파일이 아닙니다.')
    except Exception as e:
        print(f'알 수 없는 오류 발생: {e}')
    return []

def print_logs_reverse(logs):   #로그의 시간을 역순으로 출력
    for log in reversed(logs):
        print(log.strip())

def extract_problem_logs(logs, output_file):    #문제의 로그를 찾아 별도 파일로 저장
    problem_keywords = ['unstable', 'explosion', 'error', 'failure']
    problem_logs = [log for log in logs if any(keyword in log.lower() for keyword in problem_keywords)]

    with open(output_file, 'w', encoding='utf-8') as file:
        for log in problem_logs:
            file.write(log)

    print(f'문제 로그를 {output_file}에 저장했습니다.')
    return problem_logs

def md_report(problem_logs, output_file):    
    #로그에서 사고원인 분석 후 보고서 markdown파일로 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('# 사고 원인 분석 보고서\n\n')
        file.write('# > 1. 사고 로그 분석\n')

        if problem_logs:
            file.write('- **문제 로그 발견:**\n')
            for log in problem_logs:
                file.write(f'  - {log.strip()}\n')
        else:
            file.write('- 문제 로그 없음\n')

        file.write('\n# > 2. 분석 및 원인\n')
        if any('oxygen tank unstable' in log.lower() for log in problem_logs):
            file.write('- 산소 탱크 불안정으로 인해 문제가 발생함\n')
        if any('oxygen tank explosion' in log.lower() for log in problem_logs):
            file.write('- 산소 탱크 폭발이 사고의 직접적인 원인\n')
        
        file.write('\n# > 3. 개선 사항\n')
        file.write('- 산소 탱크 점검 절차 강화\n')
        file.write('- 비상 대응 시스템 개선 필요\n')

    print(f'사고 원인 분석 보고서가 {output_file}에 저장되었습니다.')

if __name__ == '__main__':
    print("Hello Mars") #설치가 잘 되었는지 확인하기 위한 출력
    f = open('mission_computer_main.log','r')
    print('\n[로그 파일 출력]\n')
    print(f.read()) #로그 파일 출력
    log_file = 'mission_computer_main.log'
    logs = read_log_file(log_file)

    if logs:
        print('\n[로그 파일 - 시간 역순 출력]\n')
        print_logs_reverse(logs)

        problem_log_file = 'problem_logs.log'
        problem_logs = extract_problem_logs(logs, problem_log_file)

        report_file = 'log_analysis.md'
        md_report(problem_logs, report_file)

