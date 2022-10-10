let chart = echarts.init(document.querySelector("#main"));
let select_countyEl = document.querySelectorAll("#select_county");
let dateEl = document.querySelector("#date");


$(document).ready(() => {
    update_time();
    get_table();
    get_table1();
});

window.onresize = function () {
    select_countyEl.resize();

};


//$("#county_btn").click(() => {
//    drawCountyPM25($("#select_county").val());
//});

$("#county_btn").click(() => {
    get_table1($("#select_county").val());
});

function weather(data) {
    dateEl.innerText = data["date"];
}

function get_table() {
    let elem = document.querySelectorAll(".select_county");
    elem.forEach(element => {
        element.addEventListener("click", e => {
            console.log(e.target.innerHTML);
            print(select_countyEl)
        });
    })

}
function get_table1() {
    const button_1 = document.getElementById("#select_county");
    alert(button_1)
}

$("#select_county").change(function () {
    county_btn = $('#select_county option:selected').val();
    $("#county_btn").val(county_btn)
})

var staval = $("#state").val(); //hidden 隱藏框的資料
$("#statenums option[value = '" + staval + "']").attr("selected", true);
