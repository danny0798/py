#tocken = 'pNvt9VOZcX2Mbuutg4QGs1-HhrpsZf98q93eTy0fdJmycQ0K_SKFRskRuyxgc6Kt';

from hs_udata import set_token, stock_list        # 引入hs_udata模块中set_token和stock_list
set_token(token = 'pNvt9VOZcX2Mbuutg4QGs1-HhrpsZf98q93eTy0fdJmycQ0K_SKFRskRuyxgc6Kt')        # 设置Token
data = stock_list()                            # 获取 股票列表数据，返回格式为dataframe
print(data.head())                                # 打印数据前5行