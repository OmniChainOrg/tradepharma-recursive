# import stripe
# import ds_bot.configs.configuration as cfg
from ds_bot.configurations import configs

# Set your secret API key
stripe.api_key = configs.configuration.TOKEN

# Function to process a payment
def process_payment(ctx,amount):
    token = "tok_visa" # replace to!!! on  valid token
    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency="usd",
            source=token,
            description="Payment for Marketplace",
        )
        await ctx.send("Payment successful ✅")
        return True
    except stripe.error.CardError as e:
        # Since it's a decline, stripe.error.CardError will be caught
        await ctx.send("Card declined: {} ❗❗".format(e))
        return False
    except stripe.error.StripeError as e:
        # Display a very generic error to the user, and maybe send
        # yourself an email
        await ctx.send("Payment failed: {} ❌".format(e))
        return False