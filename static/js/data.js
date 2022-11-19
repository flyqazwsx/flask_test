let chart = echarts.init(document.querySelector("#data"));

let no2HighSitename = document.querySelector("#no2_high_sitename");
let no2HighValue = document.querySelector("#no2_high_value");
let no2LowSitename = document.querySelector("#no2_low_sitename");
let no2LowValue = document.querySelector("#no2_low_value");


$(document).ready(() => {
    data();

});

window.onresize = function () {
    chart.resize();

};


function renderMaxno2(data) {

    let no2 = data["no2"];
    let sitename = data["sitename"];
    let maxValue = Math.max(...no2);
    let maxIndex = no2.indexOf(maxValue);
    let maxSitename = sitename[maxIndex];
    let minValue = Math.min(...no2);
    let minIndex = no2.indexOf(minValue);
    let minSitename = sitename[minIndex];
    console.log(maxSitename, maxValue);
    console.log(minSitename, minValue);

    no2HighSitename.innerText = maxSitename;
    no2HighValue.innerText = maxValue;
    no2LowSitename.innerText = minSitename;
    no2LowValue.innerText = minValue;

}


function data() {
    chart.showLoading();
    $.ajax(
        {
            url: "/data-no2",
            type: "GET",
            dataType: "json",
            success: (data) => {
                chart.hideLoading();
                drawChart(data["sitename"], data["no2"], "二氧化氮", chart, "#8b008b");
                renderMaxno2(data);
            },
            error: () => {
                chart.hideLoading();
                alert("讀取資料失敗!");
            }
        }
    );
};








function drawChart(xdata, ydata, title = "", chart = null, color = "#00008b") {
    // 指定图表的配置项和数据
    let option = {
        title: {
            text: title
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'left',
            top: 'center',
            feature: {
                magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['no2']
        },
        xAxis: {
            data: xdata,
            axisLabel: {
                inside: true,
                color: '#000000'
            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
            z: 10
        },

        yAxis: {
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                color: '#999'
            }
        },
        dataZoom: [
            {
                type: 'inside'
            },
        ],
        series: [
            {

                type: 'bar',
                showBackground: true,
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: '#83bff6' },
                        { offset: 0.5, color: '#188df0' },
                        { offset: 1, color: '#188df0' }
                    ])
                },
                emphasis: {
                    itemStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: '#2378f7' },
                            { offset: 0.7, color: '#2378f7' },
                            { offset: 1, color: '#83bff6' }
                        ])
                    }
                },
                data: ydata
            }
        ]
    };

    chart.setOption(option);

};
