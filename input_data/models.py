from djongo import models


class Quarter_data(models.Model):
    d_03 = models.IntegerField()
    d_06 = models.IntegerField()
    d_09 = models.IntegerField()
    d_12 = models.IntegerField()
    #managed=False 옵션을 주면 해당 모델은 자동으로 테이블을 생성하지 않게 된다.
    # 직접 테이블을 만들어 줘야 한다.
    class Meta:
        managed = False

class Year_data(models.Model):
    d_2019 = models.EmbeddedField(model_container = Quarter_data,)
    d_2018 = models.EmbeddedField(model_container = Quarter_data,)
    d_2017 = models.EmbeddedField(model_container = Quarter_data,)

    d_2016 = models.EmbeddedField(model_container = Quarter_data,)
    d_2015 = models.EmbeddedField(model_container = Quarter_data,)
    d_2014 = models.EmbeddedField(model_container = Quarter_data,)
    d_2013 = models.EmbeddedField(model_container = Quarter_data,)
    d_2012 = models.EmbeddedField(model_container = Quarter_data,)
    d_2011 = models.EmbeddedField(model_container = Quarter_data,)
    d_2010 = models.EmbeddedField(model_container = Quarter_data,)

    class Meta:
        managed = False

    # 재무제표 collection 안에 document 형식으로 어떻게 넣을까???
    # 외래키를 사용하자. x -->  EmbeddedField 사용하면 가능
class Financial_Statements(models.Model):
    EPS_connect = models.EmbeddedField(model_container = Year_data,)
    EPS_individual = models.EmbeddedField(model_container = Year_data,)
    PER = models.EmbeddedField(model_container = Year_data,)
    '''
    BPS = models.EmbeddedField(model_container = Year_data,)
    PBR = models.EmbeddedField(model_container = Year_data,)
    CFPS = models.EmbeddedField(model_container = Year_data,)
    PCR = models.EmbeddedField(model_container = Year_data,)
    SPS = models.EmbeddedField(model_container = Year_data,)
    PSR = models.EmbeddedField(model_container = Year_data,)
    DPS = models.EmbeddedField(model_container = Year_data,)
    Market_odds = models.EmbeddedField(model_container = Year_data,)
    ROE = models.EmbeddedField(model_container = Year_data,)
    ROS = models.EmbeddedField(model_container = Year_data,)
    S/A = models.EmbeddedField(model_container = Year_data,)
    A/E = models.EmbeddedField(model_container = Year_data,)
    ROA = models.EmbeddedField(model_container = Year_data,)
    Net_Profit_Margin = models.EmbeddedField(model_container = Year_data,)
    Sales_Operating_Margin = models.EmbeddedField(model_container = Year_data,)
    Sales_Growth_Rate = models.EmbeddedField(model_container = Year_data,)
    Operating_Profit_Growwth_Rate = models.EmbeddedField(model_container = Year_data,)
    Net_Profit_Growth_Rate = models.EmbeddedField(model_container = Year_data,)
    Equity_Capital_Growth_Rate = models.EmbeddedField(model_container = Year_data,)
    Debt_Ratio = models.EmbeddedField(model_container = Year_data,)
    Current_Ratio = models.EmbeddedField(model_container = Year_data,)
    Interest_Compensation_Magnification(Times) = models.EmbeddedField(model_container = Year_data,)
    '''