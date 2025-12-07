# Utilizing IronXL with Python License Keys

***Based on <https://ironsoftware.com/get-started/license-keys/>***


## Acquiring a License Key

Incorporating an IronXL license key enables the deployment of your applications without limitations or watermarks.

A license can be [purchased here](https://ironsoftware.com/python/excel/licensing/) or you can obtain a [complimentary 30-day trial key](https://ironsoftware.com/trial-license).

---

## Step 1: Install IronXL in Your Python Environment

To add IronXL to your Python project, you need to include it as a dependency. This is done by installing it through `pip`. Open your command-line interface and run:

```shell
pip install ironxl
```

By executing this command, IronXL is added to your project environment and is ready for use.

It's important to note that IronXL for Python is built on top of the [IronXL for .NET library](https://ironsoftware.com/csharp/excel/), and using it effectively requires the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed on your system.

---

## Step 2: Implement Your License Key

Before working with IronXL, input your purchased or trial license key at the start of your Python script:

```python
# Set up the license key

***Based on <https://ironsoftware.com/get-started/license-keys/>***

License.LicenseKey = "IRONXL-MYLICENSE-KEY-1EF01"
```

## Step 3: Confirm Your License Key

### Confirming the License Implementation

To ensure that the license key is in place, use this line of code:

```python
# Verify license application

***Based on <https://ironsoftware.com/get-started/license-keys/>***

is_licensed = License.IsLicensed
```

### License Key Validation

Confirm the effectiveness of your license key with the following code:

```python
# Validate the specific license key

***Based on <https://ironsoftware.com/get-started/license-keys/>***

is_valid = License.IsValidLicense("IRONXL-MYLICENSE-KEY-1EF01")
```

If this returns `True`, your license key is functioning correctly and you are all set to proceed. Otherwise, a `False` result indicates an issue with the key.

Ensure to rebuild and redeploy your application after setting up your license to avoid any deployment errors.

## Step 4: Launching Your IronXL Project

For those new to IronXL, we recommend reading through our [Getting Started Guide](https://ironsoftware.com/python/excel/docs/), which is packed with detailed instructions and practical examples that aid in learning how to implement IronXL in Python projects.

## Questions or Require Assistance?

While `IronXL for Python` is available for testing and development, deploying live projects requires a valid license, which you can [acquire from our licensing page](https://ironsoftware.com/python/excel/licensing/). We also offer a trial license for initial evaluations.

To explore more examples, access detailed documentation, or view licensing specifics, visit the [IronXL for Python resource](https://ironsoftware.com/python/excel/) on our site.

For further support or queries, our dedicated team is ready to help you. Feel free to [reach out to us](https://ironsoftware.com/#live-chat-support).