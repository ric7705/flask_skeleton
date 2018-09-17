var resultData;
$.ajax({
    'async': false,
    'type': "GET",
    'global': false,
    'dataType': 'json',
    'url': "/api/wallet_balance_summary",
    'success': function (data) {
        resultData = data;
    }
});

console.log(resultData)

var balance_ary = [];
var date_ary = [];

for (item in resultData) {
    date_ary.push(resultData[item].last_update)
    balance_ary.push(resultData[item].balance)
}

y_min = Math.round(Math.min.apply(null, balance_ary) * 0.75)
y_max = Math.round(Math.max.apply(null, balance_ary) * 1.25)

var cost_list = new Array(balance_ary.length).fill(549288);
var ctx = document.getElementById('invest_summary').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: date_ary,
        datasets: [{
            label: 'invest_summary',
            data: balance_ary,
            backgroundColor: "rgba(254,212,215,0.4)"
            //   backgroundColor: "rgba(153,255,51,0.4)"
        }, {
            label: 'cost',
            fill: false,
            data: cost_list,
            borderDash: [10, 5]
            //   backgroundColor: "rgba(255,153,0,0.4)"
        }
        ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    max: y_max,
                    min: y_min
                }
            }]
        }
    }
});




