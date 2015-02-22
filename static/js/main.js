function parse_stock(stock_data){
    stock_graphable={}
    //console.log(stock_data);
    date_arr=[];
    open_arr=[];
    close_arr=[];
    for (var i = 0; i < stock_data.length; i++) {
        var stock = stock_data[i];
        //for daily view
        stock.date=stock.date.split("T")[0];
        date_arr.push(stock.date);
        open_arr.push(stock.OPEN);
        close_arr.push(stock.PX_LAST);
    }
    stock_graphable['date']=date_arr;
    stock_graphable['open']=open_arr;
    stock_graphable['close']=close_arr;
    return stock_graphable;
} 


function draw_chart(stock_graphable){
    var date_arr=stock_graphable.date;
    var open_arr=['Open Price'].concat(stock_graphable.open);
    var close_arr=['Close Price'].concat(stock_graphable.close);
    var chart = c3.generate({
        data: {
                    columns: [
                open_arr,
                close_arr 
            ]
        },
        axis:{
            x: {
                type: 'category',
                categories: date_arr
            } 
        }
    });
}
