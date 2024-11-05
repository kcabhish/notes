# Running Stripe Locally

[Stripe](https://dashboard.stripe.com/test/webhooks/create?endpoint_location=local)

command to run the webhook locally

```
stripe listen --forward-to localhost:3000/api/webhooks/stripe
```
