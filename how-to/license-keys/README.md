# Using IronXL for Python License Keys

***Based on <https://ironsoftware.com/how-to/license-keys/>***


## Obtaining a License Key

To deploy your project live without any limitations or watermarks, obtaining an IronXL license key is essential.

You can [purchase a license here](https://ironsoftware.com/python/excel/licensing/) or opt for a <a class='js-modal-open' data-modal-id='trial-license'>free 30-day trial key here</a>.

<hr class="separator">

## Step 1: Install IronXL in Your Python Project

To add IronXL to your Python project, you'll need to include it as a dependency. This can be done through **pip**, the popular Python package installation tool. Open a command terminal and run:

```shell
pip install ironxl
```

This command ensures IronXL is installed and ready for use within your project.

It's important to note that IronXL for Python is built on the IronXL .NET library, which requires [.NET 6.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) to be installed on your system.

<hr class="separator">

## Step 2: Implement Your License Key

After obtaining your license, the next step is to embed your license key or trial key in your Python script. This should be done at the script's commencement before utilizing IronXL functionalities.

```python
# Inserting the license key

***Based on <https://ironsoftware.com/how-to/license-keys/>***

License.LicenseKey = "IRONXL-MYLICENSE-KEY-1EF01"
```

## Step 3: Confirm Your License Key's Functionality

### Confirm Installation of the License Key

To ensure your license key is active, you can check the **IsLicensed** property of the **License** module. Example code:

```python
# Verifying license key implementation

***Based on <https://ironsoftware.com/how-to/license-keys/>***

is_licensed = License.IsLicensed
```

### Check License Key Validity

To validate your license or trial key, use the code snippet below:

```python
# Validate the license key for accuracy

***Based on <https://ironsoftware.com/how-to/license-keys/>***

is_valid = License.IsValidLicense("IRONXL-MYLICENSE-KEY-1EF01")
```

If the result is **True**, your key is valid, and you're set to use IronXL. If **False**, the key is not valid, and further action may be required.

Ensure to clean and republish your application after updating the license key to prevent errors during deployment.

## Step 4: Begin Your Development with IronXL

Getting started with IronXL is straightforward when following our detailed [Get Started with IronXL guide](https://ironsoftware.com/python/excel/docs/). This guide offers extensive instructions and practical examples to acquaint you with IronXL's capabilities in Python projects.

## Require Assistance or Support?

While you can use `IronXL for Python` freely during development, deploying live projects requires a valid license. To [obtain a license or a trial](https://ironsoftware.com/python/excel/licensing/) and for detailed support resources, visit the [IronXL for Python section](https://ironsoftware.com/python/excel/) on our website.

Should you need further help or have questions, our dedicated team is prepared to assist. Please, feel free to [reach out to our team](#live-chat-support).