Ext.define('imct.view.xml.builder.wizard.WizardCreateChannelView', {
    extend: 'Ext.window.Window',
    xtype: 'wizard-create-channel',
    requires: ['imct.view.xml.builder.wizard.WizardCreateChannelController','imct.view.xml.builder.wizard.WizardCreateChannelModel',
        'imct.view.xml.builder.parameter.items.text.TextEditor','imct.view.xml.builder.parameter.items.date.DateEditor','imct.ChannelOrient'],
    controller: 'wizard-create-channel',
    viewModel: 'wizard-create-channel',
    modal: true,
    frame: true,
    closable: false,
    bodyPadding: 5,
    bodyBorder: true,
    layout: 'card',
    bodyPadding: 20,
    minWidth: 400,
    height: 390,
    bind: {
        activeItem: '{activeIndex}',
        title: 'Channel(s) Creation Wizard: {title}/{lastStepIndex+1}'
    },
    items: [{
        layout: {
            type: 'vbox',
            align: 'stretch',
            pack: 'start'
        },
        width: 400,
        items: [{
            xtype: 'imct-text-field',
            itemId: 'location_code',
            fieldLabel: 'Location Code',
            bind: {
                value: '{record.value}'
            }
        },{
            xtype: 'imct-date-field',
            itemId: 'start_date',
            fieldLabel: 'Start Date',
            bind: {
                value: '{record.value}'
            }
        },{
            xtype: 'imct-latitude-field',
            itemId: 'latitude',
            fieldLabel: 'Latitude',
            bind: {
                value: '{record.value}'
            }
        },{
            xtype: 'imct-longitude-field',
            itemId: 'longitude',
            fieldLabel: 'Longitude',
            bind: {
                value: '{record.value}'
            }
        },{
            xtype: 'imct-float-field',
            itemId: 'elevation',
            fieldLabel: 'Elevation',
            bind: {
                value: '{record.value}'
            }
        },{
            xtype: 'imct-float-field',
            itemId: 'depth',
            fieldLabel: 'Depth',
            bind: {
                value: '{record.value}'
            }
        }]
    },{
        layout: 'fit',
        width: 600,
        items: [{
            xtype: 'breadcrumb',
            reference: 'sensorsCmp',
            showMenuIcons: false,
            showIcons: false,
            scrollable: true,
            componentCls: 'equipment',
            displayField: 'title',
            layout: 'vbox',
            flex: 1,
            bind: {
                store: '{sensorStore}',
                selection: '{sensorSelection}'
            }
        }]
    },{
        layout: 'fit',
        width: 600,
        items: [{
            xtype: 'breadcrumb',
            reference: 'dataloggerCmp',
            showMenuIcons: false,
            componentCls: 'equipment',
            showIcons: false,
            scrollable: true,
            displayField: 'title',
            layout: 'vbox',
            flex: 1,
            bind: {
                store: '{dataloggerStore}',
                selection: '{dataloggerSelection}'
            }
        }]
    },{
        layout: {
            type: 'vbox',
            align: 'stretch',
            pack: 'start'
        },
        width: 400,
        items: [{
            xtype: 'textfield',
            fieldLabel: 'Channel Prefix',
            bind: '{codePrefix}',
            maxLength: 2,
            enforceMaxLength: true,
            allowBlank: false
        },{
            xtype: 'combobox',
            fieldLabel: 'Channel Orientation',
            bind: '{orient}',
            allowBlank: false,
            editable: false,
            displayField: 'name',
            valueField: 'id',
            allowBlank: false,
            store: {
                store: 'store.array',
                fields: ['id','name'],
                data: [[imct.ChannelOrient.ZNE,'ZNE (3 channels)'],[imct.ChannelOrient.Z12,'Z12 (3 channels)'],[imct.ChannelOrient.Z,'Z (1 channel)']]
            },
            forceSelection: true
        }]
    },{
        layout: {
            type: 'vbox',
            align: 'stretch',
            pack: 'start'
        },
        width: 400,
        items: [{
            xtype: 'fieldcontainer',
            fieldLabel: 'Channel',
            defaults: {
                flex: 1
            },
            layout: 'hbox',
            items: [{
                xtype: 'imct-text-field',
                itemId: 'code1',
                viewModel: {
                    type: 'text-editor',
                    data: {
                        nodeType: imct.NodeTypeEnum.channel
                    }
                },
                bind: {
                    value: '{record.value}'
                }
            },{
                xtype: 'imct-text-field',
                itemId: 'code2',
                bind: {
                    hidden: '{oneChannel}',
                    value: '{record.value}'
                }
            },{
                xtype: 'imct-text-field',
                itemId: 'code3',
                bind: {
                    hidden: '{oneChannel}',
                    value: '{record.value}'
                }
            }]
        },{
            xtype: 'fieldcontainer',
            fieldLabel: 'Dip',
            defaults: {
                flex: 1
            },
            layout: 'hbox',
            items: [{
                xtype: 'imct-float-field',
                itemId: 'dip1',
                bind: {
                    value: '{record.value}'
                }
            },{
                xtype: 'imct-float-field',
                itemId: 'dip2',
                bind: {
                    hidden: '{oneChannel}',
                    value: '{record.value}'
                }
            },{
                xtype: 'imct-float-field',
                itemId: 'dip3',
                bind: {
                    hidden: '{oneChannel}',
                    value: '{record.value}'
                }
            }]
        },{
            xtype: 'fieldcontainer',
            fieldLabel: 'Azimuth',
            defaults: {
                flex: 1
            },
            layout: 'hbox',
            items: [{
                xtype: 'imct-float-field',
                itemId: 'azimuth1',
                bind: {
                    value: '{record.value}'
                }
            },{
                xtype: 'imct-float-field',
                itemId: 'azimuth2',
                bind: {
                    hidden: '{oneChannel}',
                    value: '{record.value}'
                }
            },{
                xtype: 'imct-float-field',
                itemId: 'azimuth3',
                bind: {
                    hidden: '{oneChannel}',
                    value: '{record.value}'
                }
            }]
        }]
    }],
    buttons: ['->',{
        text: '&laquo; Previous',
        bind: {
            hidden: '{hiddenShowPrevious}'
        },
        handler: 'showPrevious'
    },{
        text: 'Next &raquo;',
        bind: {
            hidden: '{hiddenShowNext}'
        },
        handler: 'showNext'
    },{
        text: 'Create',
        bind: {
            hidden: '{hiddenCreate}'
        },
        handler: 'createChanel'
    }],
    tools: [{
        type: 'help',
        handler: function (){
            imct.utils.HelpUtil.helpMe('wizard_create_channel', 'Create Channel')
        }
    },{
        type: 'close',
        handler: 'onCancelClick'
    }]
});
