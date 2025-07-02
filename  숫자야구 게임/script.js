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

let attemptsLimit = 9;
let answer = []
const submitButton = document.querySelector(".submit-button");
const attemptsTime = document.getElementById("attempts");
const inputBox = document.querySelector(".input-box");


// 초기화 함수
function initializeGame() {
    // 시도 횟수 초기화
    attemptsLimit = 9;
    attemptsTime.innerText = attemptsLimit;

    //랜덤 숫자 3개 생성
    answer = [];
    while(answer.length<3){
        const random_num = Math.floor(Math.random()*10);
        if (!answer.includes(random_num)){
            answer.push(random_num);
        }
    }
    console.log(answer);

    // input 내용 비움
    EmptyInput();
    // 결과 이미지 비움
    document.getElementById("game-result-img").src = '';
    // 결과 비움
    document.querySelector(".result-display").innerHTML = '';
    // 클릭 버튼 다시 활성화
    submitButton.disabled = false;
    // 색 초기화
    document.querySelector('.remaining-attempts').style.color = 'black';
}

function EmptyInput(){
    // input 내용 비움
    document.getElementById("number1").value = '';
    document.getElementById("number2").value = '';
    document.getElementById("number3").value = '';

    document.getElementById("number1").focus();
}

// 숫자 확인 함수 
function check_numbers(){
    const num1 = document.getElementById("number1").value;
    const num2 = document.getElementById("number2").value;
    const num3 = document.getElementById("number3").value;
    const numList = [num1,num2,num3];
    
    // 숫자 3개 중 입력되지 않은 input 있으면 비우기
    if (numList.includes("")){
        numList.forEach((_,index) => {
            document.getElementById(`number${index+1}`).value = '';
        })
        document.getElementById("number1").focus();
        return;
    }

    // 숫자로 바꾸기
    const guess = numList.map(Number);

    // 숫자 비교
    let strike = 0;
    let ball = 0;
    for(let i=0;i<3;i++){
        if(guess[i]===answer[i]){
            strike += 1;
        }
        else if(answer.includes(guess[i])){
            ball += 1;
        }
    }

    displayResult(numList,strike,ball);
    
    const unique = new Set(numList);
    if (unique.size < 3) {
        // 에러 메시지 생성
        const msg = document.createElement("div");
        msg.textContent = "같은 숫자는 사용할 수 없습니다!";
        msg.style.color = "red";
        msg.style.fontWeight = "bold";
        msg.id = "error-message";
        inputBox.appendChild(msg);

        EmptyInput();

        // 1초 후 사라짐
        setTimeout(() => {
            if (msg && msg.parentNode) {
                msg.remove();
            }
        }, 1000);
    }

    EmptyInput();

    attemptsLimit--;
    attemptsTime.innerText = attemptsLimit;

    const red = 255;
    const greenBlue = Math.floor(180 * (attemptsLimit / 9)); // 점점 어두워짐

    document.querySelector('.remaining-attempts').style.color = `rgb(${red}, ${greenBlue}, ${greenBlue})`;

    // 게임 끝인지 체크 
    const resultImg = document.getElementById("game-result-img");
    // 성공
    if(strike===3){
        resultImg.src = "./success.png";
        submitButton.disabled = true;

        // 이미지 커짐
        resultImg.style.transition = "transform 0.5s ease";
        resultImg.style.transform = "scale(1.5)";

        // 0.8초 뒤 자동 리셋
        setTimeout(() => {
            initializeGame();
        }, 800);
    }
    else if(attemptsLimit===0){
        resultImg.src = "./fail.png";
        submitButton.disabled = true;

        // 이미지 작아짐
        resultImg.style.transition = "transform 0.5s ease";
        resultImg.style.transform = "scale(0.7)";

        // 0.8초 뒤 자동 리셋
        setTimeout(() => {
            initializeGame();
        }, 800);
    }



}


function displayResult(numList,strike,ball){
    const resultDisplay = document.querySelector('.result-display');
    const resultDiv = document.createElement('div');
    resultDiv.className = 'check-result';




    const leftSide = document.createElement("div");
    leftSide.classList.add("left");
    numList.forEach(num => {
        const numSpan = document.createElement("span");
        numSpan.innerText = `${num} `;
        leftSide.appendChild(numSpan);
    });

    const rightSide = document.createElement("div");
    rightSide.classList.add("right");

    if(strike===0 && ball ===0){
        const out = document.createElement("span");
        out.innerText = `O`;
        out.classList.add("out","num-result");
        rightSide.appendChild(out);
    }




    else{
        const strikeSpan = document.createElement("span");
        const strikeNum = document.createElement("span");
        strikeSpan.innerText = "S";
        strikeSpan.classList.add("strike","num-result");
        strikeNum.innerText = `${strike} `

        const ballSpan = document.createElement("span");
        const ballNum = document.createElement("span");
        ballSpan.innerText = "B";
        ballSpan.classList.add("ball","num-result");
        ballNum.innerText = ` ${ball} `



        rightSide.appendChild(strikeNum);
        rightSide.appendChild(strikeSpan);
        rightSide.appendChild(ballNum);
        rightSide.appendChild(ballSpan);

    }
    
    resultDiv.appendChild(leftSide);
    const colon = document.createElement("span");
    colon.classList.add("num-result");
    colon.innerText = " : ";
    resultDiv.appendChild(colon);
    resultDiv.appendChild(rightSide);

    resultDisplay.appendChild(resultDiv);


}


// Enter key 누르면 확인버튼 클릭
inputBox.addEventListener("keypress", (event) => {
    if (event.code === "Enter"){
        submitButton.click();
    }
});

//main
initializeGame();

// 자도 focus
["number1", "number2", "number3"].forEach((id, idx, arr) => {
  document.getElementById(id).addEventListener("input", () => {
    const input = document.getElementById(id);
    if (input.value.length === 1 && idx < arr.length - 1) {
      document.getElementById(arr[idx + 1]).focus();
    }
  });
});



// Enter key 누르면 확인버튼 클릭
// 남은 횟수 표현 구현
// 성공 실패하고 3초 뒤 자동 리셋 하기
// 한 글자 입력하면 다음 input으로 자동 이동 향상 탭 치는게 불편해서 
// 같은 숫자면 힌트처럼 에러 메세지 뜨기
