# maestro pair to Custom Core's
data = {
    "INSTANCE": {
        "COMMAND": [
            [
                "Microsoft.Compute",
                "Microsoft.Compute/snapshots/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/snapshots/delete"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/delete"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/extensions/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/extensions/delete"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/sshPublicKeys/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/sshPublicKeys/delete"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/delete"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/providers/Microsoft.Insights/diagnosticSettings/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/disks/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/disks/delete"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/availabilitySets/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/availabilitySets/delete"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/extensions/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/extensions/delete"
            ],
        ],
        "CREATE": [
            [
                "Microsoft.Compute",
                "Microsoft.Compute/snapshots/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/extensions/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/sshPublicKeys/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/providers/Microsoft.Insights/diagnosticSettings/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/disks/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/availabilitySets/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/extensions/write"
            ],
        ],
        "DELETE": [
            [
                "Microsoft.Compute",
                "Microsoft.Compute/snapshots/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/extensions/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/sshPublicKeys/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/disks/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/availabilitySets/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/extensions/delete"
            ],
        ],
        "DISABLE": [
            [
                "Microsoft.Compute",
                "Microsoft.Compute/snapshots/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/extensions/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/sshPublicKeys/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/disks/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/availabilitySets/delete"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/extensions/delete"
            ],
        ],
        "UPDATE": [
            [
                "Microsoft.Compute",
                "Microsoft.Compute/snapshots/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachines/extensions/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/sshPublicKeys/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/providers/Microsoft.Insights/diagnosticSettings/write"
            ],
            [
                "Microsoft.Compute",
                "Microsoft.Compute/disks/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/availabilitySets/write"
            ],

            [
                "Microsoft.Compute",
                "Microsoft.Compute/virtualMachineScaleSets/extensions/write"
            ],
        ]
    },
    "_ALL": {
        "_ALL": [['Microsoft.Web', 'Microsoft.Web/sites/Write'],
                 ['Microsoft.Web', 'Microsoft.Web/sites/Delete'],
                 ['Microsoft.Web', 'Microsoft.Web/sites/config/Write'],
                 ['Microsoft.Web', 'microsoft.web/sites/config/delete'],
                 ['Microsoft.Web', 'microsoft.web/sites/functions/write'],
                 ['Microsoft.Web', 'microsoft.web/sites/functions/delete'],
                 ['Microsoft.Web',
                  'microsoft.web/sites/config/web/appsettings/write'],
                 ['Microsoft.Web',
                  'microsoft.web/sites/config/web/appsettings/delete'],
                 ['Microsoft.Web',
                  'microsoft.web/sites/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Insights',
                  'Microsoft.Insights/ActivityLogAlerts/Write'],
                 ['Microsoft.Insights',
                  'Microsoft.Insights/ActivityLogAlerts/Delete'],
                 ['Microsoft.Insights',
                  'Microsoft.Insights/LogProfiles/Write'],
                 ['Microsoft.Insights',
                  'Microsoft.Insights/LogProfiles/Delete'],
                 ['Microsoft.ContainerRegistry',
                  'Microsoft.ContainerRegistry/registries/write'],
                 ['Microsoft.ContainerRegistry',
                  'Microsoft.ContainerRegistry/registries/delete'],
                 ['Microsoft.ContainerRegistry',
                  'Microsoft.ContainerRegistry/registries/privateEndpointConnections/write'],
                 ['Microsoft.ContainerRegistry',
                  'Microsoft.ContainerRegistry/registries/privateEndpointConnections/delete'],
                 ['Microsoft.CognitiveServices',
                  'Microsoft.CognitiveServices/accounts/write'],
                 ['Microsoft.CognitiveServices',
                  'Microsoft.CognitiveServices/accounts/delete'],
                 ['Microsoft.AppConfiguration',
                  'Microsoft.AppConfiguration/configurationStores/write'],
                 ['Microsoft.AppConfiguration',
                  'Microsoft.AppConfiguration/configurationStores/delete'],
                 ['Microsoft.AppConfiguration',
                  'Microsoft.AppConfiguration/configurationStores/privateEndpointConnections/write'],
                 ['Microsoft.AppConfiguration',
                  'Microsoft.AppConfiguration/configurationStores/privateEndpointConnections/delete'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/queueServices/write'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/queueServices/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/write'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/delete'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/tableServices/write'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/tableServices/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/privateEndpointConnections/write'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/privateEndpointConnections/delete'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/regeneratekey/action'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/blobServices/write'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/blobServices/delete'],
                 ['Microsoft.Storage',
                  'Microsoft.Storage/storageAccounts/blobServices/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Compute', 'Microsoft.Compute/snapshots/write'],
                 ['Microsoft.Compute', 'Microsoft.Compute/snapshots/delete'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachines/write'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachines/delete'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachines/extensions/write'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachines/extensions/delete'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/sshPublicKeys/write'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/sshPublicKeys/delete'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachineScaleSets/write'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachineScaleSets/delete'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachineScaleSets/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Compute', 'Microsoft.Compute/disks/write'],
                 ['Microsoft.Compute', 'Microsoft.Compute/disks/delete'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/availabilitySets/write'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/availabilitySets/delete'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachineScaleSets/extensions/write'],
                 ['Microsoft.Compute',
                  'Microsoft.Compute/virtualMachineScaleSets/extensions/delete'],
                 ['Microsoft.Sql', 'Microsoft.Sql/servers/write'],
                 ['Microsoft.Sql', 'Microsoft.Sql/servers/delete'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/encryptionProtector/write'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/administrators/write'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/administrators/delete'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/advancedThreatProtectionSettings/write'],
                 ['Microsoft.Sql', 'Microsoft.Sql/servers/databases/write'],
                 ['Microsoft.Sql', 'Microsoft.Sql/servers/databases/delete'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/databases/transparentDataEncryption/write'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/vulnerabilityAssessments/write'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/vulnerabilityAssessments/delete'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/failoverGroups/write'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/failoverGroups/delete'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/servers/auditingSettings/write'],
                 ['Microsoft.Sql', 'Microsoft.Sql/managedInstances/write'],
                 ['Microsoft.Sql', 'Microsoft.Sql/managedInstances/delete'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/managedInstances/encryptionProtector/write'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/managedInstances/securityAlertPolicies/write'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/managedInstances/vulnerabilityAssessments/write'],
                 ['Microsoft.Sql',
                  'Microsoft.Sql/managedInstances/vulnerabilityAssessments/delete'],
                 ['Microsoft.Kusto', 'Microsoft.Kusto/Clusters/write'],
                 ['Microsoft.Kusto', 'Microsoft.Kusto/Clusters/delete'],
                 ['Microsoft.Security',
                  'Microsoft.Security/autoProvisioningSettings/write'],
                 ['Microsoft.Security', 'Microsoft.Security/pricings/write'],
                 ['Microsoft.Security', 'Microsoft.Security/pricings/delete'],
                 ['Microsoft.Security', 'Microsoft.Security/settings/write'],
                 ['Microsoft.Security',
                  'Microsoft.Security/securityContacts/write'],
                 ['Microsoft.Security',
                  'Microsoft.Security/securityContacts/delete'],
                 ['Microsoft.Security',
                  'Microsoft.Security/locations/jitNetworkAccessPolicies/write'],
                 ['Microsoft.Security',
                  'Microsoft.Security/locations/jitNetworkAccessPolicies/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/frontDoorWebApplicationFirewallPolicies/write'],
                 ['Microsoft.Network',
                  'Microsoft.Network/frontDoorWebApplicationFirewallPolicies/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkSecurityGroups/write'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkSecurityGroups/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkSecurityGroups/securityRules/write'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkSecurityGroups/securityRules/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkSecurityGroups/join/action'],
                 ['Microsoft.Network',
                  'Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies/write'],
                 ['Microsoft.Network',
                  'Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkWatchers/flowLogs/write'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkWatchers/flowLogs/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkWatchers/configureFlowLog/action'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkWatchers/write'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkWatchers/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/applicationGateways/write'],
                 ['Microsoft.Network',
                  'Microsoft.Network/applicationGateways/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkInterfaces/write'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkInterfaces/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/virtualNetworks/write'],
                 ['Microsoft.Network', 'virtualNetworks/delete'],
                 ['Microsoft.Network',
                  'Microsoft.Network/networkInterfaces/join/action'],
                 ['Microsoft.Network', 'Microsoft.Network/frontDoors/write'],
                 ['Microsoft.Network', 'Microsoft.Network/frontDoors/delete'],
                 ['Microsoft.ServiceFabric',
                  'Microsoft.ServiceFabric/clusters/write'],
                 ['Microsoft.ServiceFabric',
                  'Microsoft.ServiceFabric/clusters/delete'],
                 ['Microsoft.DataFactory',
                  'Microsoft.DataFactory/datafactories/write'],
                 ['Microsoft.DataFactory',
                  'Microsoft.DataFactory/datafactories/delete'],
                 ['Microsoft.DocumentDB',
                  'Microsoft.DocumentDB/databaseAccounts/write'],
                 ['Microsoft.DocumentDB',
                  'Microsoft.DocumentDB/databaseAccounts/delete'],
                 ['Microsoft.DocumentDB',
                  'Microsoft.DocumentDB/databaseAccounts/privateEndpointConnections/write'],
                 ['Microsoft.DocumentDB',
                  'Microsoft.DocumentDB/databaseAccounts/privateEndpointConnections/delete'],
                 ['Microsoft.DBforPostgreSQL',
                  'Microsoft.DBforPostgreSQL/servers/write'],
                 ['Microsoft.DBforPostgreSQL',
                  'Microsoft.DBforPostgreSQL/servers/delete'],
                 ['Microsoft.DBforPostgreSQL',
                  'Microsoft.DBforPostgreSQL/servers/configurations/write'],
                 ['Microsoft.DBforPostgreSQL',
                  'Microsoft.DBforPostgreSQL/servers/securityAlertPolicies/write'],
                 ['Microsoft.DBforPostgreSQL',
                  'Microsoft.DBforPostgreSQL/servers/privateEndpointConnections/write'],
                 ['Microsoft.DBforPostgreSQL',
                  'Microsoft.DBforPostgreSQL/servers/privateEndpointConnections/delete'],
                 ['Microsoft.DBforPostgreSQL',
                  'Microsoft.DBforPostgreSQL/servers/firewallRules/write'],
                 ['Microsoft.DBforPostgreSQL',
                  'Microsoft.DBforPostgreSQL/servers/firewallRules/delete'],
                 ['Microsoft.Authorization',
                  'Microsoft.Authorization/diagnosticSettings/write'],
                 ['Microsoft.Authorization',
                  'Microsoft.Authorization/diagnosticSettings/delete'],
                 ['Microsoft.Authorization',
                  'Microsoft.Authorization/roleDefinitions/write'],
                 ['Microsoft.Authorization',
                  'Microsoft.Authorization/roleDefinitions/delete'],
                 ['Microsoft.DBforMySQL',
                  'Microsoft.DBforMySQL/servers/write'],
                 ['Microsoft.DBforMySQL',
                  'Microsoft.DBforMySQL/servers/delete'],
                 ['Microsoft.DBforMySQL',
                  'Microsoft.DBforMySQL/servers/securityAlertPolicies/write'],
                 ['Microsoft.DBforMySQL',
                  'Microsoft.DBforMySQL/servers/configurations/write'],
                 ['Microsoft.DBforMySQL',
                  'Microsoft.DBforMySQL/servers/privateEndpointConnections/write'],
                 ['Microsoft.DBforMySQL',
                  'Microsoft.DBforMySQL/servers/privateEndpointConnections/delete'],
                 ['Microsoft.Logic',
                  'Microsoft.Logic/workflows/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.ServiceBus',
                  'Microsoft.ServiceBus/namespaces/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.ContainerService',
                  'Microsoft.ContainerService/containerServices/write'],
                 ['Microsoft.ContainerService',
                  'Microsoft.ContainerService/containerServices/delete'],
                 ['Microsoft.ContainerService',
                  'Microsoft.ContainerService/managedClusters/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Synapse', 'Microsoft.Synapse/workspaces/write'],
                 ['Microsoft.Synapse', 'Microsoft.Synapse/workspaces/delete'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/keys/write'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/keys/delete'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/keys/purge/action'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/keys/update/action'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/keys/create/action'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/keys/import/action'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/keys/recover/action'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/keys/restore/action'],
                 ['Microsoft.KeyVault', 'Microsoft.KeyVault/vaults/write'],
                 ['Microsoft.KeyVault', 'Microsoft.KeyVault/vaults/delete'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/privateEndpointConnections/write'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/privateEndpointConnections/delete'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/providers/Microsoft.Insights/diagnosticSettings/Write'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/secrets/write'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/secrets/delete'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/secrets/purge/action'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/secrets/update/action'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/secrets/recover/action'],
                 ['Microsoft.KeyVault',
                  'Microsoft.KeyVault/vaults/secrets/restore/action'],
                 ['Microsoft.MachineLearningServices',
                  'Microsoft.MachineLearningServices/workspaces/write'],
                 ['Microsoft.MachineLearningServices',
                  'Microsoft.MachineLearningServices/workspaces/delete'],
                 ['Microsoft.MachineLearningServices',
                  'Microsoft.MachineLearningServices/workspaces/computes/write'],
                 ['Microsoft.MachineLearningServices',
                  'Microsoft.MachineLearningServices/workspaces/computes/delete'],
                 ['Microsoft.MachineLearningServices',
                  'Microsoft.MachineLearningServices/workspaces/privateEndpointConnections/write'],
                 ['Microsoft.MachineLearningServices',
                  'Microsoft.MachineLearningServices/workspaces/privateEndpointConnections/delete'],
                 ['Microsoft.DBforMariaDB',
                  'Microsoft.DBforMariaDB/servers/write'],
                 ['Microsoft.DBforMariaDB',
                  'Microsoft.DBforMariaDB/servers/delete'],
                 ['Microsoft.DBforMariaDB',
                  'Microsoft.DBforMariaDB/servers/privateEndpointConnections/write'],
                 ['Microsoft.DBforMariaDB',
                  'Microsoft.DBforMariaDB/servers/privateEndpointConnections/delete'],
                 ['Microsoft.DataLakeAnalytics',
                  'Microsoft.DataLakeAnalytics/accounts/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.ApiManagement',
                  'Microsoft.ApiManagement/service/certificates/write'],
                 ['Microsoft.ApiManagement',
                  'Microsoft.ApiManagement/service/certificates/delete'],
                 ['Microsoft.ApiManagement',
                  'Microsoft.ApiManagement/service/write'],
                 ['Microsoft.ApiManagement',
                  'Microsoft.ApiManagement/service/delete'],
                 ['Microsoft.ApiManagement',
                  'Microsoft.ApiManagement/service/tags/write'],
                 ['Microsoft.ApiManagement',
                  'Microsoft.ApiManagement/service/tags/delete'],
                 ['Microsoft.RecoveryServices',
                  'Microsoft.RecoveryServices/Locations/backupProtectedItem/write'],
                 ['Microsoft.EventHub', 'Microsoft.EventHub/namespaces/write'],
                 ['Microsoft.EventHub',
                  'Microsoft.EventHub/namespaces/delete'],
                 ['Microsoft.EventHub',
                  'Microsoft.EventHub/namespaces/privateEndpointConnections/write'],
                 ['Microsoft.EventHub',
                  'Microsoft.EventHub/namespaces/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Devices',
                  'Microsoft.Devices/IotHubs/diagnosticSettings/write'],
                 ['Microsoft.Devices', 'Microsoft.Devices/iotHubs/Write'],
                 ['Microsoft.Devices', 'Microsoft.Devices/iotHubs/Delete'],
                 ['Microsoft.Cache', 'Microsoft.Cache/redis/write'],
                 ['Microsoft.Cache', 'Microsoft.Cache/redis/delete'],
                 ['Microsoft.Cache',
                  'Microsoft.Cache/redis/firewallRules/write'],
                 ['Microsoft.Cache',
                  'Microsoft.Cache/redis/firewallRules/delete'],
                 ['Microsoft.Search',
                  'Microsoft.Search/searchServices/diagnosticSettings/write'],
                 ['Microsoft.Batch',
                  'Microsoft.Batch/batchAccounts/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Batch', 'Microsoft.Batch/batchAccounts/write'],
                 ['Microsoft.Batch', 'Microsoft.Batch/batchAccounts/delete'],
                 ['Microsoft.EventGrid', 'Microsoft.EventGrid/domains/write'],
                 ['Microsoft.EventGrid', 'Microsoft.EventGrid/domains/delete'],
                 ['Microsoft.EventGrid',
                  'Microsoft.EventGrid/domains/privateEndpointConnections/write'],
                 ['Microsoft.EventGrid',
                  'Microsoft.EventGrid/domains/privateEndpointConnections/delete'],
                 ['Microsoft.EventGrid', 'Microsoft.EventGrid/topics/write'],
                 ['Microsoft.EventGrid', 'Microsoft.EventGrid/topics/delete'],
                 ['Microsoft.EventGrid',
                  'Microsoft.EventGrid/topics/privateEndpointConnections/write'],
                 ['Microsoft.EventGrid',
                  'Microsoft.EventGrid/topics/privateEndpointConnections/delete'],
                 ['Microsoft.AppPlatform',
                  'Microsoft.AppPlatform/Spring/write'],
                 ['Microsoft.AppPlatform',
                  'Microsoft.AppPlatform/Spring/delete'],
                 ['Microsoft.SignalRService',
                  'Microsoft.SignalRService/SignalR/write'],
                 ['Microsoft.SignalRService',
                  'Microsoft.SignalRService/SignalR/delete'],
                 ['Microsoft.SignalRService',
                  'Microsoft.SignalRService/SignalR/privateEndpointConnections/write'],
                 ['Microsoft.SignalRService',
                  'Microsoft.SignalRService/SignalR/privateEndpointConnections/delete'],
                 ['Microsoft.StreamAnalytics',
                  'Microsoft.StreamAnalytics/streamingjobs/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Databricks',
                  'Microsoft.Databricks/workspaces/write'],
                 ['Microsoft.Databricks',
                  'Microsoft.Databricks/workspaces/delete'],
                 ['Microsoft.DataLakeStore',
                  'Microsoft.DataLakeStore/accounts/providers/Microsoft.Insights/diagnosticSettings/write'],
                 ['Microsoft.Automation',
                  'Microsoft.Automation/automationAccounts/variables/write'],
                 ['Microsoft.Automation',
                  'Microsoft.Automation/automationAccounts/variables/delete']]

    }
}
