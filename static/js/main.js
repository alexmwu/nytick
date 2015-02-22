function parse_stock(stock_data){
    stock_graphable={}
    for stock in stock_data:
        var date = stock["date"]
        console.log(date);

} 


var chart = c3.generate({
        data: {
                    columns: [
                ['data1', 30, 200, 100, 400, 150, 250],
                ['data2', 50, 20, 10, 40, 15, 25]
            ]
        }
});
