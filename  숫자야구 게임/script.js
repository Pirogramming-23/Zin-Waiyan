// Game Rules
// 0~9 사이의 랜덤 숫자 3개 정한다
// 순서가 올바른 숫자 3개를 찾는다
    // 숫자 틀림, 위치 틀림 -> 아웃 O
    // 숫자 맞음, 위치 틈림 -> 볼 +1
    // 숫자 맞음, 위치 맞음 -> 스트라이크 +1
// 스트라이크 3 -> 승리 이미지 출력
// 9번의 기회가 끝나면 -> 패배 이미지 출력


// TODO 
// 게임 초기화
    // 시도 횟수 초기화 : 가능 회수 = 9
    // 랜덤 숫자 3개 생성 (중복 안 됨)
    // html input & 결과창 내용 비움
// 숫자 확인 - check_numbers() 구현 
    // 숫자 3개 중 입력되지 않은 input 있으면 -> input창 비움(숫자 확인하지 않음)
    // 숫자 3개 다 입력 되면 
        // 입력된 숫자들 === 정답 -> 결과 생성 -> html 업데이트
        // 게임 끝인지 체크 
            // 승리 이미지 or 패배 이미지 출력 (game-result-img 태그 사용)
            // 확인하지 버튼 비활성화

// 남은 횟수 출력

let attempts = 9;
let answer = []

// 초기화 함수
function initializeGame() {
    // 시도 횟수 초기화
    attempts = 9;
    document.getElementById("attempts").innerText = attempts;

    //랜덤 숫자 3개 생성
    answer = [];
    while(answer.length<3){
        const random_num = Math.floor(Math.random()*10);
        if (!(answer.includes(random_num))){
            answer.push(random_num);
        }
    }

    // input 내용 비움
    document.getElementById("number1").value = '';
    document.getElementById("number2").value = '';
    document.getElementById("number3").value = '';
    // 결과 이미지 비움
    document.getElementById("game-result-img").src = '';
    // 결과 비움
    document.getElementById("results").innerHTML = '';
    // 클릭 버튼 다시 활성화
    document.querySelector(".submit-button").disabled = false;
}

// 숫자 확인 함수 
