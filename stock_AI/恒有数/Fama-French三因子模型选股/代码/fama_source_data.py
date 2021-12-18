import hs_udata as hs
import pandas as pd


# 获取从开始日期到目前日期的每个月的最后一个交易日
def get_trade_dates(token, start_date):
    hs.set_token(token)
    trade_date = hs.trading_calendar(secu_market='83',
                                     if_trading_day='1',
                                     if_month_end='1',
                                     start_date=start_date)
    print(trade_date.head())
    return trade_date


# 获取记录A股上市、退市股票交易代码、股票名称、上市状态等信息；
def get_stock_a(token):
    hs.set_token(token)
    # 默认取全部，1-上市，2-终止;
    listed_state = "1"
    fields = "secu_code,chi_name,hs_code,secu_market,listed_sector"
    stock_datas = hs.stock_list(listed_state, fields)
    print(stock_datas.head())
    return stock_datas


# 获取 交易日期 股票行情，公司等信息
def get_stock_month_trade(token, secu_code, trade_date):
    hs.set_token(token)

    # 获取股票交易信息
    # 获取数据:证劵代码,交易日期,开盘价,最高价,收盘价,涨跌幅,成交数量,成交额,换手率,涨跌停状态,交易状态
    stock_fields = "prod_code,trading_date,open_price,high_price,close_price,px_change_rate," \
                   "business_amount,business_balance,turnover_ratio,up_down_status,turnover_status"
    stock_data = hs.stock_quote_daily(en_prod_code=secu_code,
                                      trading_date=trade_date,
                                      adjust_way=2,
                                      fields=stock_fields)

    # 获取公司估值等信息
    # 获取数据：证劵代码,交易日期,总市值,总市值（证监会算法）,市净率PB（最新财报，LF）,市盈率（最新年报，LYR）
    value_fields = "prod_code,total_market_value,total_market_value_zjh,pb_lf,pe_rate_lyr"
    value_data = hs.valuation_info(en_prod_code=secu_code,
                                   trading_date=trade_date,
                                   fields=value_fields)
    # print(stock_data.head())
    # print(value_data.head())
    res_data = pd.merge(stock_data, value_data, how='left', on='prod_code')
    print(res_data.head())
    res_data.rename(columns={'trading_date': '交易日期',
                             'prod_code': '证劵代码',
                             'open_price': '开盘价',
                             'high_price': '最高价',
                             'close_price': '收盘价',
                             'px_change_rate': '涨跌幅',
                             'business_amount': '成交数量',
                             'business_balance': '成交额',
                             'turnover_ratio': '换手率',
                             'up_down_status': '涨跌停状态',
                             'turnover_status': '交易状态',
                             'total_market_value': '总市值',
                             'total_market_value_zjh': '总市值（证监会算法）',
                             'pb_lf': '市净率PB（最新财报，LF）',
                             'pe_rate_lyr': '市盈率（最新年报，LYR）'},
                    inplace=True)
    return res_data


# 查询从2018-11-01到目前所有A股上市公司，月末交易数据
def get_astock_data(token):
    res_data = pd.DataFrame()
    loop = 0
    # 获取交易日期
    trade_date_list = get_trade_dates(token, "2018-11-01")
    # 获取所有A股正常状态公司信息
    stock_datas = get_stock_a(token)
    stock_code = ""
    for stock in stock_datas["hs_code"]:
        stock_code = stock_code + ',' + stock
        if loop >= 500:
            loop = 0
            for trade_date in trade_date_list["trading_date"]:
                if res_data.size == 0:
                    res_data = get_stock_month_trade(token, stock_code, trade_date)
                    res_data.to_csv("strategy/fama/temp/source_output.csv", mode='w', index=False, encoding="gbk")
                else:
                    res_data = get_stock_month_trade(token, stock_code, trade_date)
                    res_data.to_csv("strategy/fama/temp/source_output.csv", mode='a', index=False, encoding="gbk")
            stock_code = ""
        else:
            loop = loop + 1
    print(res_data.head())
    res_data.to_csv("strategy/fama/temp/source_output.csv", mode='a', index=False, encoding="gbk")
