def r_file(divide):
    try:
        with open(divide, "r", encoding="utf-8") as f:
            return [{"timestamp": line.split(",", 1)[0], "message": line.split(",", 1)[1].strip()} for line in f if "," in line]
    except Exception as err:
        print(f"파일 오류: {err}")
        return []
    
def list_dict(data): #리스트를 딕셔너리로 전환환
    return {str(i): d for i, d in enumerate(data)}

def s_json(write_j, data):
    try:
        with open(write_j, "w", encoding="utf-8") as f:
            f.write("{\n" + ",\n".join(f'    "{i}": {{"timestamp": "{d["timestamp"]}", "message": "{d["message"]}"}}' for i, d in data.items()) + "\n}\n")
    except Exception as err:
        print(f"JSON 저장 중 오류 발생: {err}")

def input_keyword(logs, keyword):
    return [log for log in logs if keyword.lower() in log['message'].lower()]

if __name__ == "__main__":
    log_file = "mission_computer_main.log"
    j_file = "mission_computer_main.json"
    
    try:
        with open(log_file,"r") as f:
            print("로그 출력",f.read())
    except Exception as err:
        print(f"파일 읽기 오류: {err}")
        exit()
    
    logs = r_file(log_file)
    
    if logs:
        print("전환된 리스트 출력\n",logs) #전환된 리스트 출력
        logs.sort(reverse=True, key=lambda x: x["timestamp"])#리스트 시간기준으로 역순 정렬
        logs_dict=list_dict(logs)
        s_json(j_file, logs_dict)
        
        keyword = input("검색할 문자열을 입력하세요: ")
        filtered_logs = input_keyword(logs, keyword)
        
        if filtered_logs:
            print(f"'{keyword}' 포함된 로그 메시지:")
            for log in filtered_logs:
                print(f"Timestamp: {log['timestamp']}, Message: {log['message']}")
        else:
            print(f"'{keyword}' 키워드가 포함된 로그가 없습니다.")
    else:
        print("로그 파일을 읽을 수 없습니다.")
