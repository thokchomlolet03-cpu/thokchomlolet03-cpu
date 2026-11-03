# Enterprise endpoints — Windows, macOS, Intune, Jamf

Professional relevance: user has prior enterprise support exposure to Microsoft 365, Active Directory, Entra ID, Intune, Jamf, SCCM, ServiceNow and secure connectivity. The goal is to advance from ticket resolution to **understanding policy architecture, device lifecycle and safe fleet automation**.

## Windows / Microsoft
**Understand:** Windows boot, services, event channels, Windows Update, user profiles, NTFS permissions, process tree, registry, BitLocker, certificate stores, DNS and trust chain.

**Manage:** AD DS vs Microsoft Entra ID, hybrid identity, device enrollment, Intune configuration, device compliance, Conditional Access, app packaging, updates, Autopilot, Group Policy vs modern management, Endpoint Privilege Management.

**Diagnose:** difference between Windows logon, Entra sign-in, Kerberos, DNS, VPN, proxy, firewall and application issues. Learn Sysinternals, event logs, `gpresult`, `dsregcmd /status`, Microsoft Graph PowerShell (authorized only). Don't publish tenant/user data.

## macOS / Apple
**Understand:** XNU, launchd, APFS, application signing/notarization, Gatekeeper, FileVault, TCC privacy, certificates, profiles, unified logging and hardware security.

**Manage:** supervised/managed device fundamentals, Apple Business Manager organization enrollment, automated enrollment, MDM push/commands, declared management, configuration profiles, inventory, patching, software deployment, retirement.

**Jamf Pro learning sequence:**
1. Free [Jamf 100](https://www.jamf.com/training/100-course/) and interactive simulations.
2. [Apple Platform Deployment](https://support.apple.com/guide/deployment/welcome/web) and [Apple Platform Security](https://support.apple.com/guide/security/welcome/web).
3. Document lifecycle and policy examples in a mock architecture.
4. When permitted, conduct real tests using a personal Mac and an appropriate Jamf trial/organizational tenant, under vendor licensing and Apple enrollment rules.
5. Consider [Jamf 200](https://www.jamf.com/training/200-course/) only if employment value and financial support justify it.

**Important:** Jamf 100 screenshots or examples are not evidence that you administered a production fleet. Some Apple MDM paths cannot be meaningfully validated without eligible hardware, organizational enrollment and an authorized tenant.

## Project P08: cross-platform endpoint lifecycle
Create two clearly separated cases: (A) a real, legal test environment with observable outcomes; (B) architecture-only designs for inaccessible MDM capabilities. Cover provisioning, identity, least privilege, inventory, security policy, software deployment, update/patch, compliance, remediation and secure retirement. Explicitly label each case.

## Certifications
See [MD-102, Jamf 100 and Apple credentials](CERTIFICATIONS.md). Certifications complement, but never substitute for, lab evidence and real work.

Official references: [Intune](https://learn.microsoft.com/en-us/intune/) · [Entra](https://learn.microsoft.com/en-us/entra/) · [Microsoft Graph](https://learn.microsoft.com/en-us/graph/) · [Apple IT Training](https://training.apple.com/) · [Jamf](https://www.jamf.com/training/).
