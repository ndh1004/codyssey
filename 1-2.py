def r_file(divide):
    try:
        with open(divide, "r", encoding="utf-8") as f:
            return [{"timestamp": line.split(",", 1)[0], "message": line.split(",", 1)[1].strip()} for line in f if "," in line]
    except Exception as err:
        print(f"파일 오류: {err}")
        return []

def s_json(write_j, data):
    try:
        with open(write_j, "w", encoding="utf-8") as f:
            f.write("{\n" + ",\n".join(f'    "{i}": {{"timestamp": "{d["timestamp"]}", "message": "{d["message"]}"}}' for i, d in enumerate(data)) + "\n}\n")
    except Exception as err:
        print(f"JSON 저장 중 오류 발생: {err}")

def input_keyword(logs, keyword):
    return [log for log in logs if keyword.lower() in log['message'].lower()]

if __name__ == "__main__":
    
    f=open("mission_computer_main.log")
    print("로그 출력",f.read()) #로그출력
    log_file = "mission_computer_main.log"
    j_file = "mission_computer_main.json"
    logs = r_file(log_file)
    
    if logs:
        print("전환된 리스트 출력\n",logs) #전환된 리스트 출력
        logs.sort(reverse=True, key=lambda x: x["timestamp"])#리스트 시간기준으로 역순 정렬
        s_json(j_file, logs)
        
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
