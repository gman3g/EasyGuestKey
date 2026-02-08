# Running Notes

## Create a restricted user

### Create a group with limited rights

```text
/user group
add name=wifi-automation policy=api,password,read,sensitive,ssh,test,write,!local,!policy,!reboot,!sniff,!telnet
```

### Create the user

```text
/user
add name=EasyGuestBot group=wifi-automation comment="GCP Cloud Function Service Account"
```

## SSH Key

### 1. Generate the Key Pair

Open PowerShell and run the following command:

```powershell
ssh-keygen -t ed25519 -f "$HOME\.ssh\mikrotik_gcp_key" -C "gcp-automation"
```

- -t ed25519: Specifies the modern, high-security algorithm.

- -f ...: Saves it to a specific file so it doesn't overwrite your default keys.

- -C ...: Adds a comment so you can identify the key in WinBox later.

- Passphrase: When it asks for one, leave it blank (press Enter twice). Since your Python script needs to run unattended, it can't prompt for a password.

### 2. Locate the Files
This created two files in your .ssh folder:

1. mikrotik_gcp_key: Your Private Key. This goes into your GCP Secret Manager.

2. mikrotik_gcp_key.pub: Your Public Key. This is what you upload to the MikroTik.

### 3. Import to the hAP ax³

Open WinBox and go to Files.

Drag and drop mikrotik_gcp_key.pub into the WinBox file list.

Go to System → Users → SSH Keys.

Click Import SSH Key.

Select the User you created for automation.

Select the Key File (mikrotik_gcp_key.pub) and click Import.