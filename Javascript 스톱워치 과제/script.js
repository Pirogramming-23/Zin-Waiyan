
const display = document.getElementById("display");

let timer = null;
let startTime = 0;
let elapsedTime = 0;
let running = false;
let id=0;


function start(){
    if(!running){
        // Date.now() : 지금 시간
        startTime = Date.now() - elapsedTime;
        // 10 milliseconds마다 update 함수 부르기
        timer = setInterval(update,1);
        running = true;
    }
}

function stop(){
    if(running){
        // update 함수 부르기를 멈춘다
        clearInterval(timer);
        const currentTime = Date.now();
        elapsedTime = currentTime-startTime;
        // second, milliseconds 로 바뀌기
        let seconds = Math.floor(elapsedTime/1000%60);
        let milliseconds = Math.floor(elapsedTime%1000/10);
        // 0 두개 붙이기
        seconds = String(seconds).padStart(2,"0");
        milliseconds = String(milliseconds).padStart(2,"0");

        id++;
        running = false;
        createRecord(`${id}`,`${seconds} : ${milliseconds}`);
        attachCheckboxListeners();
    }
}

function reset(){
    clearInterval(timer);
    startTime = 0;
    elapsedTime = 0;
    running = false;
    display.textContent = "00 : 00";
}


// 전체 선택 기능 
const recordHeadCheckbox = document.getElementById("record__head");
recordHeadCheckbox.addEventListener("change", () => {
  const records = document.querySelectorAll(".record__content input[type='checkbox']");
  records.forEach(input => {
    input.checked = recordHeadCheckbox.checked;
  });
});


// 전체 선택 버튼 구현
function updateHeaderCheckbox() {
  const recordCheckboxes = document.querySelectorAll(".record__content input[type='checkbox']");
  const allChecked = Array.from(recordCheckboxes).every(input => input.checked);

  // 다 체크 -> 헤더 체크
  // 다 안 체크 -> 헤더 안 체크
  if (allChecked) {
    recordHeadCheckbox.checked = true;
  } else {
    recordHeadCheckbox.checked = false;
  }
}
function attachCheckboxListeners() {
  const recordCheckboxes = document.querySelectorAll(".record__content input[type='checkbox']");
  recordCheckboxes.forEach(input => {
    input.addEventListener("change", updateHeaderCheckbox);
  });
}


function deleteRecord(){
    const records = document.querySelectorAll(".record__content");

    // 선택 삭제 기능 구현
    records.forEach(record=>{
        const input = record.querySelector("input[type='checkbox']");
        if(input && input.checked){
            record.remove();
        }
    });
}


function createRecord(id,Text){
    // <!-- <div id="record_1" class="record__content">
    //             <input type="checkbox" id="record1">
    //             <label for="record1"></label>
    //             <div></div> 
    //         </div> -->

    // Record content
    const record_content = document.createElement("div")
    record_content.id = `record_${id}`;
    record_content.className = "record__content";

    // input
    const input = document.createElement("input");
    input.type = "checkbox";
    input.id = `record${id}`;

    // label
    const label = document.createElement("label");
    label.setAttribute("for",`record${id}`);
    label.textContent = Text;

    //placeholder Div
    const emptyDiv = document.createElement("div");
    emptyDiv.className = "emptyDiv";

    record_content.appendChild(input);
    record_content.appendChild(label);
    record_content.appendChild(emptyDiv);
    
    const record_container = document.querySelector(".record__container");
    record_container.appendChild(record_content);

}

function update(){
    const currentTime = Date.now();
    elapsedTime = currentTime-startTime;

    // second, milliseconds 로 바뀌기
    let seconds = Math.floor(elapsedTime/1000%60);
    let milliseconds = Math.floor(elapsedTime%1000/10);

    // 0 두개 붙이기
    seconds = String(seconds).padStart(2,"0");
    milliseconds = String(milliseconds).padStart(2,"0");

    display.textContent = `${seconds} : ${milliseconds}`;
}




