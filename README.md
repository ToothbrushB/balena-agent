# balena-agent

If you're looking for a way to quickly and easily get up and running with an Kerberos Agent for your home network, this is the project for you.

This project is a [balenaCloud](https://www.balena.io/cloud) stack with the following services:

- [Kerberos Agent](https://github.com/kerberos-io/agent) is a cutting edge video surveillance management system made available as Open Source under the MIT License.

balenaCloud is a free service to remotely manage and update your IoT devices through an online dashboard interface, as well as providing remote access to the Kerberos Agent web interface without any additional configuation.

## Getting Started

You can one-click-deploy this project to balena using the button below:

[![deploy with balena](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/kerberos-io/agent)

## Manual Deployment

Alternatively, deployment can be carried out by manually creating a [balenaCloud account](https://dashboard.balena-cloud.com) and application,
flashing a device, downloading the project and pushing it via the [balena CLI](https://github.com/balena-io/balena-cli).

### Application Environment Variables

Application environment variables apply to all services within the application, and can be applied fleet-wide to apply to multiple devices.

| Name           | Description                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------- |
| `SET_HOSTNAME` | Set a custom hostname on application start. Default is `kerberos-agent`.                                                |

## Usage

### Initial setup

Once your device joins the fleet you'll need to allow some time for it to download the application.

On your router or DHCP server assign a static IP to your AdGuard Home device.

1. Connect to `http://YOUR-DEVICE-IP` or depending on the hostname `http://kerberos-agent.local` in your browser
2. Sign-in with the default username and password `root`, `root`.

Documentation for Adguard Home can be found at https://doc.kerberos.io/