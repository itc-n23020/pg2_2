import random
import time
from threading import Thread

def ask_question(a, b, timeout=8):
    answer = a * b
    attempts = 3
    start_time = time.time()
    result = False
    
    while attempts > 0:
        print(f"{a} x {b} = ?")
        
        user_answer = None
        def get_user_input():
            nonlocal user_answer
            user_answer = input("Your answer: ")
        
        input_thread = Thread(target=get_user_input)
        input_thread.start()
        input_thread.join(timeout)
        
        if user_answer is None:
            print("時間切れ！次の問題に移ります。")
            return False
        
        if user_answer.isdigit() and int(user_answer) == answer:
            print("正解！")
            time.sleep(1)
            return True
        else:
            print("不正解です。もう一度試してください。")
            attempts -= 1
        
        if time.time() - start_time > timeout:
            print("時間切れ！次の問題に移ります。")
            return False
    
    print(f"正しい答えは {answer} でした。")
    return False

def multiplication_quiz():
    correct_answers = 0
    total_questions = 10
    
    for _ in range(total_questions):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        if ask_question(a, b):
            correct_answers += 1
    
    print(f"\nクイズ終了！")
    print(f"正解数: {correct_answers}/{total_questions}")

if __name__ == "__main__":
    multiplication_quiz()

