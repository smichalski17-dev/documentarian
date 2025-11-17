---
title: "Kubernetes Installation"
linkTitle: "Kubernetes Installation"
description: >
  Follow this process to install Certifai in Kubernetes.
---
## Installation Prerequisites

- Kubernetes version v1.16 or greater
- Docker CLI configured with permissions to push to the docker registry used by the Kubernetes cluster
- Certifai Enterprise Archive (Zip) file obtained from your CognitiveScale Certifai Sales Representative
- Linux/OSX Control machine to run the installation script with a few dependencies needed that are described in the Certifai Enterprise Installation section
- A command line yaml processor - 
- Credentials for a PostgreSQL database (We recommend PostgreSQL 13.x) to setup the Reporting ETL job for scan reports and policy checks
- Credentials and bucket details for one of AWS S3, GCP GCS, Azure BlobStorage; these details are needed later while setting up the Certifai Custom Resource on Kubernetes

## Certifai Enterprise Configuration

The default Certifai Installation script creates a Certifai Enterprise subscription in the `certifai` namespace by default. You can change this behavior by editing the following files:

<!-- - CatalogSource - Edit catalog-source and update the following fields:
  * `namespace` - the namespace you want to install the operator into
- OperatorGroup - Edit operator-group.yaml and update the following fields:
  * `namespace` - The namespace you want to install the operator into
  * `spec.targetNamespaces` - Single element list containing the namespace used earlier
- Subscription - Edit subscription.yaml and set the following fields:
  * `namespace` - The namespace you want to install the operator into
  * `channel` - This should be set to `stable`. Check with your CognitiveScale representative for options if you'd like to run `beta` releases
  * `installPlanApproval` - Set to `automatic`
  * `sourceNamespace` - The namespace where the CatalogSource was created.
  * `startingCSV`: You may want to change this if you're planning to run a `beta` release. Check with your CognitiveScale representative for suggestions if you're not running the `stable` channel -->
- Cluster Roles for Subject Access Reviews - Edit the file named `gke-rbac-clusterroles.yaml`:
  *  `subjects.namespace` the namespace you want to install Certifai Enterprise into

## Certifai Enterprise Installation

Run the installation script:
```
./install-offline.sh -u <DOCKER USER> -p <DOCKER REGISTRY PASSWORD> -r <DOCKER REGISTRY URL> -n <NAMESPACE> -m
```




## Create an instance of Certifai Enterprise

If you are using LDAP integration, do that integration now before creating and applying the `certifai-cr.yaml` file.

:::important

In this section we first configure a Certifai Enterprise installation (Operand / Application) in the namespace supplied during the Enterprise installation.

:::

Create a new file called `certifai-cr.yaml` with the following YAML content:

```yaml
apiVersion: cortex.cognitivescale.com/v1
kind: Certifai
metadata:
  name: default-certifai
  # namespace should match the namespace set in the subscription defined earlier in the Enterprise Configuration section
  namespace: certifai
spec:
  deployment-type: k8s
  dex:
    #enable dex to act as the oidc provider
    enabled: true
    create-ingress: true
    replicas: 1
    #dex auth provider connector
    connector:
      type: github
      name: Github
      client-id: github oauth app client id
      client-secret: github oauth app client secret
      #additional configurations as found in https://github.com/dexidp/website/tree/main/content/docs/connectors
      add-config: |
        orgs:
        - name: org-to-provide access to
  console:
    create-ingress: true
    replicas: 1
    route-type: oauth
    authorization-type: rbac
    s3:
      access-key: your access key
      endpoint: 'https://s3.amazonaws.com'
      secret-key: your secret key
      verify-cert: false
    scan-dir: path to the storage bucket or container
  reference-model:
    enabled: true
  policy:
    create-ingress: true
    s3:
      access-key: your access key
      endpoint: 'https://s3.amazonaws.com'
      secret-key: your secret key
      verify-cert: false
    enabled: true
    questionnaire-dir: path to the storage bucket or container
    policy-control-config-file: path to the control config yaml file
    authorization-type: rbac
    replicas: 1
    route-type: oauth
  scan-manager:
    enabled: false
    create-ingress: true
    replicas: 1
    scan-data-dir: ""
    ingress-config:
      max-body-size: 1000m
      proxy-connect-timeout: "180"
      proxy-read-timeout: "180"
  reporting:
    enabled: true
    period: "*/15 * * * *"
    db-conn-str: "postgresql://user:password@service:port/db"
  monitoring:
    enabled: true
    period: '*/15 * * * *'
    monitoring-dir: ""
  rai-center:
    enabled: true
    create-ingress: false
    replicas: 1
    db-conn-str: "postgresql://user:password@service:port/db"
    rai-reports-dir: ""
```

Edit the following spec/dex parameters:

- `spec/deployment-type`
- `spec/dex/enabled`
- `spec/dex/replicas`
- `spec/dex/connector/type`
- `spec/dex/connector/name`
- `spec/dex/connector/client-id`
- `spec/dex/connector/client-secret`
- `spec/dex/connector/add-config`
- `spec/console/gcs/application-credentials`
- `spec/console/route-type`: Set this to `oauth` if `spec.dex.enabled` is set to `true`
- `spec/console/authorization-type`: Set this to `rbac` if `spec.dex.enabled` is set to true
- `spec/console/azure/account-name`
- `spec/console/azure/account-key`
- `spec/console/azure/sas-token`
- `spec/console/s3/access-key`
- `spec/console/s3/endpoint`
- `spec/console/s3/secret-key`
- `spec/console/scan-dir`
- `spec/policy/enabled`
- `spec/policy/route-type`: Set this to `oauth` if `spec.dex.enabled` is set to `true`
- `spec/policy/authorization-type`: Set this to `rbac` if `spec.dex.enabled` is set to true
- `spec/policy/gcs/application-credentials`
- `spec/policy/azure/account-name`
- `spec/policy/azure/account-key`
- `spec/policy/azure/sas-token`
- `spec/policy/s3/access-key`
- `spec/policy/s3/endpoint`
- `spec/policy/s3/secret-key`
- `spec/policy/questionnaire-dir`
- `spec/scan-manager/enabled`
- `spec/scan-manager/replicas`
- `spec/scan-manager/scan-data-dir`
- `spec/scan-manager/ingress-config/max-body-size`
- `spec/scan-manager/ingress-config/proxy-connect-timeout`
- `spec/scan-manager/ingress-config/proxy-read-timeout`
- `spec/reference-model/enabled`
- `spec/reporting/enabled`
- `spec/reporting/period`
- `spec/reporting/db-conn-str`
- `spec/monitoring/enabled`
- `spec/monitoring/period`
- `spec/monitoring/monitoring-dir`
- `spec/rai-center/enabled`
- `spec/rai-center/create-ingress`
- `spec/rai-center/replicas`
- `spec/rai-center/db-conn-str`
- `spec/rai-center/rai-reports-dir`

| Parameter | Description | Example |
| --- | --- | ---|
| `apiVersion` | APIVersion defines the versioned schema of this representation of an object. Should NOT be changed by users. | `cortex.cognitivescale.com/v1` |
| `kind` | Identifies the package type you are installing | (Always) `Certifai` |
| `metadata/name` | The name of your installation as configured | `default-certifai` |
| `metadata/namespace` | The namespace you selected in the Subscription section of the Enterprise Configuration section above | `certifai` |
| `spec/deployment-type` | Options are: <br/>`gke`: This guide is for GKE so this is the only option that works here. | default = `openshift` |
| `spec/dex/enabled` | Enable Dex as an authentication provider to access the Certifai Console and remote CLI operations. | default = `false`; set this to `true` |
| `spec/dex/connector/type` | Dex connector type: Should be one of the options described at https://dexidp.io/docs/connectors/  | `github` |
| `spec/dex/connector/name` | The name of the Dex connector. Can be set to a sane value of your choice. Required field when Dex is enabled | your-dex-connector-name |
| `spec/dex/connector/client-id` | oauth app client ID for the Dex connector of your choice. Required field when Dex is enabled | `your-oauth-provider-client-id` |
| `spec/dex/connector/client-secret` | oauth app client secret for the Dex connector of your choice. Required field when Dex is enabled | `your-oauth-provider-client-secret` |
| `spec/dex/connector/add-config` | Additional configuration (yaml) you may want to pass on to Dex, including specific organization, teams etc. Refer to the documentation for connectors. All fields, excluding client ID, client Secret and redirectURI, maybe specified in this section. Optional field when Dex is enabled | orgs: <br/>- name: organization-with-certifai-access |
| `spec/console/replicas` | The number of console instances you want your organization to run concurrently | default = `2` |
| `spec/console/route-type` | Console access options are: <br/>`none` (default): no authentication is required to open the Console <br/>  `http`: Unsecured for a closed network <br/> `https`: Secured for the internet <br/> `oauth`: Enables login with Dex connector credentials | default = `none`  |
| `spec/console/authorization-type` | If Dex is enabled and you want to control access to the Certifai Console, set this field to `rbac`. Otherwise, the Certifai Console will have unauthenticated access | default = `none` |
| `spec/console/scan-dir` | A path-like string prefixed with `gs://` for `gcs` storage, `abfs://` for Azure Storage Accounts and `s3://` for S3 / Ceph / Noobaa storage accounts  | `scan-dir` |
| `spec/console/gcs/application-credentials` | JSON content of the application credentials file for a service account obtained from GCP. This needs to be a JSON key and not P12. | `application-credentials` |
| `spec/console/s3/access-key` | The s3 (or Ceph) access key you configured during your infrastructure setup | `access-key` |
| `spec/console/s3/endpoint` | The s3 (or noobaa/Ceph) endpoint you configured during your infrastructure setup | `s3.amazonaws.com` |
| `spec/console/s3/secret-key` | The s3 (or Ceph) secret-key you configured during your infrastructure setup |  `s3secret1234` |
| `spec/console/azure/account-name` | The name of your Azure Storage Account with Blob containers | `account-name` |
| `spec/console/azure/account-key` | An account key for a Blob Container present in the `account-name` referenced above | `account-key` |
| `spec/console/azure/sas-token` | An SAS token for a Blob Container present in the `account-name` referenced above | `sas-token` |
| `spec/policy/replicas` | The number of policy instances you want your organization to run concurrently | default = `2` |
| `spec/policy/route-type` | Policy Access options are: <br/>`none` (default): no authentication is required to open the policy<br/>`http`: Unsecured for a closed network<br/>`https`: Secured for the internet<br/>`oauth`: Enables login with Dex connector credentials | default=`none`  |
| `spec/policy/authorization-type` | If dex is enabled, and you want to control access to the Certifai policy, set this field to `rbac`. Otherwise, the Certifai policy will have unauthenticated access | default = `none` |
| `spec/policy/questionnaire-dir` | A path-like string prefixed with `gs://` for `gcs` storage, `abfs://` for Azure Storage Accounts and `s3://` for S3 / Ceph / Noobaa storage accounts  | `scan-dir` |
| `spec/policy/policy-control-config-file` | A path-like string (yaml file) prefixed with `gs://` for `gcs` storage, `abfs://` for Azure Storage Accounts and `s3://` for S3 / Ceph / Noobaa storage accounts  | `policy-control-config-file` |
| `spec/policy/gcs/application-credentials` | JSON content of the application credentials file for a service account obtained from GCP. This needs to be a JSON key and not P12. | `application-credentials` |
| `spec/policy/s3/access-key` | The s3 (or Ceph) access key you configured during your infrastructure setup | `access-key` |
| `spec/policy/s3/endpoint` | The s3 (or noobaa/Ceph) endpoint you configured during your infrastructure setup | `s3.amazonaws.com` |
| `spec/policy/s3/secret-key` | The s3 (or Ceph) secret-key you configured during your infrastructure setup |  `s3secret1234` |
| `spec/policy/azure/account-name` | The name of your Azure Storage Account with Blob containers | `account-name` |
| `spec/policy/azure/account-key` | An account key for a Blob Container present in the `account-name` referenced above | `account-key` |
| `spec/policy/azure/sas-token` | An SAS token for a Blob Container present in the `account-name` referenced above | `sas-token` |
| `spec/scan-manager/replicas` | The number of scan manager instances you want your organization to run concurrently | default = `2` |
| `spec/scan-manager/enabled` | Boolean. Enables or disables scan manager instances that is added to your installation. Users may disable the scan manager at any time to remove it from the installation to save resources. | default = `false` |
| `spec/scan-manager/scan-data-dir` | A path-like string prefixed with `gs://` for `gcs` storage, `abfs://` for Azure Storage Accounts and `s3://` for S3 / Ceph / Noobaa storage accounts  | `scan-data-dir` |
| `spec/scan-manager/ingress-config/max-body-size` | Size of the client request body; Uses `m` as units. (Optional) | `1000m` (megabytes) |
| `spec/scan-manager/ingress-config/proxy-connect-timeout` | Proxy connect timeout for connections to the upstream servers. (Optional)  | `"180"` (seconds) |
| `spec/scan-manager/ingress-config/proxy-read-timeout` | Proxy read timeout for connections to the upstream servers (Optional) | `"180"` (seconds) |
| `spec/reference-model/enabled` | Boolean. Enables or disables the reference model server that is added to your installation. Users may disable the reference model at any time to remove it from the installation to save resources. | default = `true` |
| `spec/reporting/enabled` | Boolean. Enables or disables the reporting ETL job that is added to your installation. Users may disable the reporting ETL job at any time to remove it from the installation to save resources. | default = `true` |
| `spec/reporting/period` | Cron time string describing how often the reporting ETL job should run. The default value is 15 minutes.| default = `*/15 * * * *` |
| `spec/reporting/db-conn-str` | PostgreSQL connection string.  The location the reporting ETL will load report data to.| default = `postgresql://user:password@service:port/db` |
| `spec/monitoring/enabled` | Boolean. Enables or disables the runtime monitoring job that is added to your installation. Users may disable the monitoring job at any time to remove it from the installation to save resources. | default = `true` |
| `spec/monitoring/period`  | Cron time string describing how often the monitoring job should run. The default value is 15 minutes.| default = `*/15 * * * *` |
| `spec/monitoring/monitoring-dir`  | A path-like string prefixed with gs:// for gcs storage, abfs:// for Azure storage accounts and s3:// for S3 / Ceph / Noobaa storage accounts | `monitoring-dir` |
| `spec/rai-center/enabled` | Boolean. Enables or disables RAI Center instances that is added to your installation. Users may disable the RAI Center at any time to remove it from the installation to save resources. | default = `false` |
| `spec/rai-center/replicas` | The number of RAI Center instances you want your organization to run concurrently | default = `1` |
| `spec/rai-center/db-conn-str` | PostgreSQL connection string.  The location the RAI Center loads data to and fetches data from.| default = `postgresql://user:password@service:port/db` |
| `spec/rai-center/rai-reports-dir` | A path-like string prefixed with gs:// for gcs storage, abfs:// for Azure storage accounts and s3:// for S3 / Ceph / Noobaa storage accounts | `rai-reports-dir` |

The `spec.dex` section of the above YAML snippet connects an OAuth application of an authentication provider of your choice (supported by Dex) to enable authentication and RBAC of this Cortex Certifai installation.

Apply this custom resource to the namespace you created in the Configuration section above using
```
kubectl apply -f certifai-cr.yaml -n <your_namespace>
```
