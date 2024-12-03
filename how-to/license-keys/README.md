# Using IronXL for Python License Keys

***Based on <https://ironsoftware.com/how-to/license-keys/>***


## How to Acquire a License Key

Obtaining an IronXL license key enables the deployment of your project in a live environment free from any limitations or watermarking.

You can [purchase a license here](https://ironsoftware.com/python/excel/licensing/) or obtain a [free 30 day trial key here](trial-license).

---

## Step 1: Incorporate IronXL as a Dependency in Your Python Project

To add IronXL to your Python project, you should install it through **pip**. In your command line interface, input the following:

```shell
pip install ironxl
```

This command ensures IronXL is installed in your system and available for import. IronXL for Python utilizes the IronXL .NET library, based on .NET 6.0. Make sure the [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) is installed on your computer to use IronXL for Python efficiently.

---

## Step 2: Implement Your License Key

Initially, you should input your license or trial key by setting up the `LicenseKey` attribute within your Python script, prior to using IronXL functionalities.

```python
# Initialize your license key

***Based on <https://ironsoftware.com/how-to/license-keys/>***

License.LicenseKey = "IRONXL-MYLICENSE-KEY-1EF01"
```

## Step 3: Confirm Your License Key

### Examine the Activated License Key

To ensure your license key is properly set up, examine the `IsLicensed` attribute from the `License` module:

```python
# Verify the licensing status

***Based on <https://ironsoftware.com/how-to/license-keys/>***

is_licensed = License.IsLicensed
```

### Check License Key Validity

For verifying the validity of your license or trial key, utilize the code below:

```python
# Validate the license key

***Based on <https://ironsoftware.com/how-to/license-keys/>***

is_valid = License.IsValidLicense("IRONXL-MYLICENSE-KEY-1EF01")
```

If `is_valid` is **True**, the key is correctly set and you're all set to proceed with IronXL. Conversely, a **False** return means the key is invalid.

It's crucial to clean and republish your application after insertions for ensured functionality and to prevent potential errors.

## Step 4: Initiate Your Project

To optimize your IronXL utilization, we strongly advise following our in-depth [Get Started with IronXL](https://ironsoftware.com/python/excel/docs/) guide. This guide offers extensive insights and examples critical for mastering IronXL usage in Python projects.

## Questions or Require Assistance?

Throughout the development stage, IronXL for Python is at your disposal, albeit requiring a license for actual deployments. License purchases and a trial version are available [here](https://ironsoftware.com/python/excel/licensing/). For further information, code samples, and rich documentation, visit our [IronXL for Python page](https://ironsoftware.com/python/excel/).

Our expert team is available to provide additional support or answer any questions. Feel free to [contact our support team](#live-chat-support).