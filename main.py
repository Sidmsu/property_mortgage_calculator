NUMBER_OF_PAYMENTS = 360
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

WELCOME_TEXT = '''\nMORTGAGE PLANNING CALCULATOR\n============================ '''
MAIN_PROMPT = '''\nEnter a value for each of the following items or type 'NA' if unknown '''
print(WELCOME_TEXT)
print(MAIN_PROMPT)
LOCATIONS_TEXT = input('''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? ''')
SQUARE_FOOTAGE_TEXT = (input('''\nWhat is the maximum square footage you are considering? '''))
MAX_MONTHLY_PAYMENT_TEXT = (input('''\nWhat is the maximum monthly payment you can afford? '''))
DOWN_PAYMENT_TEXT = int(input('''\nHow much money can you put down as a down payment? '''))
APR_TEXT =(input('''\nWhat is the current annual percentage rate? '''))


PRICE = 0
OUTPUT_TEXT = '''\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.
A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:,.1f}% APR results
\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'''
output_text = ('\n\nIn {}, a maximum monthly payment of ${} allows the purchase of a house of {} sq. feet for ${} '
'\t assuming a 30-year fixed rate mortgage with a ${} down payment at {}% APR.')
KEEP_GOING_TEXT = 'y'
while True:

    if LOCATIONS_TEXT.lower() == 'seattle':
        PRICE_PER_SQ_FOOT = SEATTLE_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = SEATTLE_PROPERTY_TAX_RATE
    elif LOCATIONS_TEXT.lower() == 'san francisco':
        PRICE_PER_SQ_FOOT = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = SAN_FRANCISCO_PROPERTY_TAX_RATE
    elif LOCATIONS_TEXT.lower() == 'austin':
        PRICE_PER_SQ_FOOT = AUSTIN_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = AUSTIN_PROPERTY_TAX_RATE
    elif LOCATIONS_TEXT.lower() == 'east lansing':
        PRICE_PER_SQ_FOOT = EAST_LANSING_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = EAST_LANSING_PROPERTY_TAX_RATE
    else:
        LOCATIONS_TEXT='the average U.S. housing market'
        LOCATION_NOT_KNOWN_TEXT ='''\nUnknown location. Using national averages for price per square foot and tax rate.'''
        print(LOCATION_NOT_KNOWN_TEXT)
        PRICE_PER_SQ_FOOT = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = AVERAGE_NATIONAL_PROPERTY_TAX_RATE



    if APR_TEXT =="NA":
        APR_TEXT = APR_2023*100
    else:
        APR_TEXT = float(APR_TEXT)

    if SQUARE_FOOTAGE_TEXT == 'NA' and MAX_MONTHLY_PAYMENT_TEXT != 'NA':

        output_text = ("\n\nIn {}, a maximum monthly payment of ${:,.2F} allows the purchase of a house of {:,.0F} sq. feet for ${:,.0F} \n"
        "\tassuming a 30-year fixed rate mortgage with a ${:,.0F} down payment at {:.1F}% APR.")
        APR_MONTHLY = APR_TEXT / 12 / 100
        SQUARE_FOOTAGE_NA=100
        while True:
            ESTIMATED_HOME_COST = (SQUARE_FOOTAGE_NA * PRICE_PER_SQ_FOOT)
            PRICE = ESTIMATED_HOME_COST - DOWN_PAYMENT_TEXT
            APR_MONTHLY=APR_TEXT/12/100
            MONTHLY_PAYMENT = PRICE * (
                        APR_MONTHLY / (1 - (1 + APR_MONTHLY) ** -NUMBER_OF_PAYMENTS))
            MONTHLY_TAX = ESTIMATED_HOME_COST * PROPERTY_TAX_RATE / 12
            FINAL_PAYMENT= MONTHLY_TAX + MONTHLY_PAYMENT
            if FINAL_PAYMENT > float(MAX_MONTHLY_PAYMENT_TEXT):
                SQUARE_FOOTAGE_NA -= 1
                break
            SQUARE_FOOTAGE_NA += 1
        print(output_text.format(LOCATIONS_TEXT, float(MAX_MONTHLY_PAYMENT_TEXT), float(SQUARE_FOOTAGE_NA),
                             float(ESTIMATED_HOME_COST-PRICE_PER_SQ_FOOT), float(DOWN_PAYMENT_TEXT), float(APR_TEXT)))
        KEEP_GOING_TEXT = input('''\nWould you like to make another attempt (Y or N)? ''')
        if KEEP_GOING_TEXT.lower() != 'y':
            break
        else:
            print(WELCOME_TEXT)
            print(MAIN_PROMPT)
            LOCATIONS_TEXT = input(
                '''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? ''')
            SQUARE_FOOTAGE_TEXT = (input('''\nWhat is the maximum square footage you are considering? '''))
            MAX_MONTHLY_PAYMENT_TEXT = (input('''\nWhat is the maximum monthly payment you can afford? '''))
            DOWN_PAYMENT_TEXT = int(input('''\nHow much money can you put down as a down payment? '''))
            APR_TEXT = (input('''\nWhat is the current annual percentage rate? '''))

    elif SQUARE_FOOTAGE_TEXT!='NA' and MAX_MONTHLY_PAYMENT_TEXT=='NA':
        SQUARE_FOOTAGE_TEXT = float(SQUARE_FOOTAGE_TEXT)
        PRICE = SQUARE_FOOTAGE_TEXT * PRICE_PER_SQ_FOOT


        APR_MONTHLY = APR_TEXT / 12 / 100
        PRICE_PAY = PRICE - DOWN_PAYMENT_TEXT
        MONTHLY_PAYMENTS = ((PRICE_PAY * ((APR_MONTHLY) * (1 + APR_MONTHLY) ** NUMBER_OF_PAYMENTS)) /
                            (((1 + APR_MONTHLY) ** NUMBER_OF_PAYMENTS) - 1))
        PROPERTY_TAX = (PRICE * PROPERTY_TAX_RATE) / 12
        FINAL_PAYMENT = MONTHLY_PAYMENTS + PROPERTY_TAX
        print(OUTPUT_TEXT.format(LOCATIONS_TEXT, float(SQUARE_FOOTAGE_TEXT), float(PRICE), float(DOWN_PAYMENT_TEXT),
                                 float(APR_TEXT),
                                 float(PROPERTY_TAX), float(MONTHLY_PAYMENTS), float(FINAL_PAYMENT)))
        '''\n\nIn {}, an average {:,.0f} sq. foot house would cost ${:,.0f}.
        A 30-year fixed rate mortgage with a down payment of ${:,.0f} at {:,.1f}% APR results
        \tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}'''

    elif SQUARE_FOOTAGE_TEXT!='NA' and MAX_MONTHLY_PAYMENT_TEXT!='NA':
        SQUARE_FOOTAGE_TEXT = float(SQUARE_FOOTAGE_TEXT)
        PRICE = SQUARE_FOOTAGE_TEXT * PRICE_PER_SQ_FOOT
        MAX_MONTHLY_PAYMENT_TEXT = float(MAX_MONTHLY_PAYMENT_TEXT)

        APR_MONTHLY = APR_TEXT / 12 / 100
        PRICE_PAY = PRICE - DOWN_PAYMENT_TEXT
        MONTHLY_PAYMENTS = ((PRICE_PAY * ((APR_MONTHLY) * (1 + APR_MONTHLY) ** NUMBER_OF_PAYMENTS)) /
                            (((1 + APR_MONTHLY) ** NUMBER_OF_PAYMENTS) - 1))
        PROPERTY_TAX = (PRICE * PROPERTY_TAX_RATE) / 12
        FINAL_PAYMENT = MONTHLY_PAYMENTS + PROPERTY_TAX
        print(OUTPUT_TEXT.format(LOCATIONS_TEXT, float(SQUARE_FOOTAGE_TEXT), float(PRICE), float(DOWN_PAYMENT_TEXT),
                                 float(APR_TEXT),
                                 float(PROPERTY_TAX), float(MONTHLY_PAYMENTS), float(FINAL_PAYMENT)))
        if FINAL_PAYMENT > MAX_MONTHLY_PAYMENT_TEXT:
            print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'
                  .format(MAX_MONTHLY_PAYMENT_TEXT))
        else:
            print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'
                  .format(MAX_MONTHLY_PAYMENT_TEXT))

    else:
        NOT_ENOUGH_INFORMATION_TEXT = '''\nYou must either supply a desired square footage or a maximum monthly payment.
        Please try again.'''
        print(NOT_ENOUGH_INFORMATION_TEXT)



    #Amortization Table
    AMORTIZATION_TEXT = input('''\nWould you like to print the monthly payment schedule (Y or N)? ''')
    if AMORTIZATION_TEXT.lower() == 'y':
        print('\n{:^7}|{:^12}|{:^13}|{:^13}'.format('Month', 'Interest', 'Payment', '   Balance    '))
        print("================================================")
        PRICE_PAY = PRICE - DOWN_PAYMENT_TEXT
        BALANCE = PRICE_PAY
        APR_MONTHLY = APR_TEXT / 12 / 100
        MONTHLY_PAYMENTS = ((PRICE_PAY * ((APR_MONTHLY) * (1 + APR_MONTHLY) ** NUMBER_OF_PAYMENTS)) /
                            (((1 + APR_MONTHLY) ** NUMBER_OF_PAYMENTS) - 1))
        PRINCIPAL = MONTHLY_PAYMENTS
        for MONTH in range(1,NUMBER_OF_PAYMENTS+1):
            INTEREST = APR_MONTHLY * BALANCE
            PRINCIPAL = MONTHLY_PAYMENTS - INTEREST
            INTEREST = round(float(INTEREST),5)
            print('{:^7,.0f}| ${:>9,.2f} | ${:>10,.2f} | $ {:>10,.2f}'.format(MONTH, INTEREST, PRINCIPAL, BALANCE))
            BALANCE -= PRINCIPAL

        KEEP_GOING_TEXT = input('''\nWould you like to make another attempt (Y or N)? ''')
        if KEEP_GOING_TEXT.lower() != 'y':
            break
        else:
            print(WELCOME_TEXT)
            print(MAIN_PROMPT)
            LOCATIONS_TEXT = input(
                '''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? ''')
            SQUARE_FOOTAGE_TEXT = (input('''\nWhat is the maximum square footage you are considering? '''))
            MAX_MONTHLY_PAYMENT_TEXT = (input('''\nWhat is the maximum monthly payment you can afford? '''))
            DOWN_PAYMENT_TEXT = int(input('''\nHow much money can you put down as a down payment? '''))
            APR_TEXT = (input('''\nWhat is the current annual percentage rate? '''))
