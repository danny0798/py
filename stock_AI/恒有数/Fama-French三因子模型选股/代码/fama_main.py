import pandas as pd


# 计算法码三因子模型数据
def get_fama_stock():
    # 导入数据源数据
    stock_source = pd.read_csv(filepath_or_buffer='strategy/fama/temp/source_output.csv',
                               parse_dates=['交易日期'],
                               encoding='gbk')
    # 计算股票下个月涨跌幅
    stock_source['下月涨跌幅'] = stock_source.groupby('证劵代码')['涨跌幅'].shift(-1)

    # 删除一些不满足基础要求数据
    # 1.删除在市净率小手0的股票
    stock_source.dropna(subset=['市净率PB（最新财报，LF）'], inplace=True)
    stock_source = stock_source[stock_source['市净率PB（最新财报，LF）'] > 0]
    # 2.删除在当月最后一个交易日停牌的股票
    stock_source.dropna(subset=['交易状态'], inplace=True)
    stock_source = stock_source[stock_source['交易状态'] == '交易']
    # 3.删除在当月最后一个交易日涨停的股票
    stock_source = stock_source[stock_source['涨跌停状态'] != '涨停']
    # 4.删除在当月最后一个交易日跌停的股票
    stock_source = stock_source[stock_source['涨跌停状态'] != '跌停']
    # 5.删除下月涨跌幅为空的数据
    stock_source.dropna(subset=['下月涨跌幅'], inplace=True)

    # 开始选股
    stock_source['因子'] = stock_source['总市值']*stock_source['市净率PB（最新财报，LF）']
    stock_source = stock_source.sort_values(by=['交易日期', '因子'])
    stock_source = stock_source.groupby(['交易日期']).head(10)

    # 计算收益
    invest = pd.DataFrame()
    stock_source['证劵代码'] += ' '
    stock_data = stock_source.groupby('交易日期')
    invest['买入股票'] = stock_data['证劵代码'].sum()
    invest['股票数量'] = stock_data.size()
    invest['买入股票下周平均涨幅（%）'] = stock_data['下月涨跌幅'].mean()
    invest['下个月资金（初始资金100元）'] = (invest['买入股票下周平均涨幅（%）']+1.0).cumprod()*100
    invest.reset_index(inplace=True)



