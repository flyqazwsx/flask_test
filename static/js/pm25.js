let chart1 = echarts.init(document.querySelector("#pm25"));

let pm25HighSitename = document.querySelector("#pm25_high_sitename");
let pm25HighValue = document.querySelector("#pm25_high_value");
let pm25LowSitename = document.querySelector("#pm25_low_sitename");
let pm25LowValue = document.querySelector("#pm25_low_value");

$(document).ready(() => {
    pm25();
});

window.onresize = function () {
    chart1.resize();
};





function pm25() {
    chart1.showLoading();
    $.ajax(
        {
            url: "/data-pm25",
            type: "GET",
            dataType: "json",
            success: (data) => {
                chart1.hideLoading();
                drawChart(data["sitename"], data["pm25"], "細懸浮微粒", chart1, "#8b008b");
                renderMaxpm25(data);
            },
            error: () => {
                chart1.hideLoading();
                alert("讀取資料失敗!");
            }
        }
    );
};



function renderMaxpm25(data) {

    let pm25 = data["pm25"];
    let sitename = data["sitename"];
    let maxValue = Math.max(...pm25);
    let maxIndex = pm25.indexOf(maxValue);
    let maxSitename = sitename[maxIndex];
    let minValue = Math.min(...pm25);
    let minIndex = pm25.indexOf(minValue);
    let minSitename = sitename[minIndex];
    console.log(maxSitename, maxValue);
    console.log(minSitename, minValue);

    pm25HighSitename.innerText = maxSitename;
    pm25HighValue.innerText = maxValue;
    pm25LowSitename.innerText = minSitename;
    pm25LowValue.innerText = minValue;

}



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
