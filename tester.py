from nsepy import get_history
from datetime import date

nifty = get_history(symbol="sbin",
                    start=date(2015,1,1),
                    end=date(2015,1,10),
					index=False)
# nifty[['Close', 'Turnover']].plot(secondary_y='Turnover')
# print(nifty.columns)


eq = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        option_type="CE",
                        strike_price=300,
                        expiry_date=date(2015,1,29))
print(eq.columns)