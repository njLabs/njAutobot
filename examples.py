from nsepy import get_history
from datetime import date

startDate = date(2020,11,20)
endDate = date(2020,11,26)
expiry = date(2020,11,26)

sbin = get_history(symbol='SBIN',
                   start=date(2015,1,1),
                   end=date(2015,1,10))

# Stock futures (Similarly for index futures, set index = True)
stock_fut = get_history(symbol="SBIN",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            futures=True,
                            expiry_date=date(2015,1,29))

# Stock options (Similarly for index options, set index = True)
stock_opt = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        option_type="CE",
                        strike_price=300,
                        expiry_date=date(2015,1,29))

# NIFTY Next 50 index
nifty_next50 = get_history(symbol="NIFTY NEXT 50",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            index=True)
# NIFTY50 Equal wight index (random index from the list)
nifty_eq_wt = get_history(symbol="NIFTY50 EQUAL WEIGHT",
                            start=date(2017,6,1),
                            end=date(2017,6,10),
                            index=True)

nifty_fut = get_history(symbol="NIFTY",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        index=True,
                        futures=True,
                        expiry_date=date(2015,1,29))

nifty_opt = get_history(symbol="NIFTY",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        index=True,
                        option_type='CE',
                        strike_price=8200,
                        expiry_date=date(2015,1,29))

vix = get_history(symbol="INDIAVIX",
            start=date(2015,1,1),
            end=date(2015,1,10),
            index=True)

from nsepy.derivatives import get_expiry_date
expiry = get_expiry_date(year=2015, month=1)

stock_opt = get_history(symbol="SBIN",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            futures=True,
                            expiry_date=get_expiry_date(2015,1))

# Index P/E ratio history
from nsepy import get_index_pe_history
nifty_pe = get_index_pe_history(symbol="NIFTY",
                                start=date(2015,1,1),
                                end=date(2015,1,10))

# USD, GBP, EURO, YEN to INR rbi reference rates:
from nsepy import get_rbi_ref_history
rbi_ref = get_rbi_ref_history(date(2015,1,1), date(2015,1,10))

# Download daily bhav copy, which is nothing but OHLC prices of all the traded stocks on a particular day:
from nsepy.history import get_price_list
prices = get_price_list(dt=date(2015,1,1))