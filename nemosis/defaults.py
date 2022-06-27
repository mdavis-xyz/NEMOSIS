names = {'FCAS Providers': 'NEM Registration and Exemption List.xls',
         'DISPATCHLOAD': 'PUBLIC_DVD_DISPATCHLOAD',
         'DUDETAILSUMMARY': 'PUBLIC_DVD_DUDETAILSUMMARY',
         'DUDETAIL': 'PUBLIC_DVD_DUDETAIL',
         'DISPATCHCONSTRAINT': 'PUBLIC_DVD_DISPATCHCONSTRAINT',
         'GENCONDATA': 'PUBLIC_DVD_GENCONDATA',
         'DISPATCH_UNIT_SCADA': 'PUBLIC_DVD_DISPATCH_UNIT_SCADA',
         'DISPATCHPRICE': 'PUBLIC_DVD_DISPATCHPRICE',
         'SPDREGIONCONSTRAINT': 'PUBLIC_DVD_SPDREGIONCONSTRAINT',
         'SPDCONNECTIONPOINTCONSTRAINT': 'PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT',
         'SPDINTERCONNECTORCONSTRAINT': 'PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT',
         'BIDPEROFFER_D': 'PUBLIC_DVD_BIDPEROFFER_D',
         'DISPATCHINTERCONNECTORRES': 'PUBLIC_DVD_DISPATCHINTERCONNECTORRES',
         'BIDDAYOFFER_D': 'PUBLIC_DVD_BIDDAYOFFER_D',
         'DISPATCHREGIONSUM': 'PUBLIC_DVD_DISPATCHREGIONSUM',
         'FCAS_4_SECOND': 'FCAS',
         'ELEMENTS_FCAS_4_SECOND': 'Elements_FCAS.csv',
         'VARIABLES_FCAS_4_SECOND': 'Ancillary Services Market Causer Pays Variables File.csv',
         'Generators and Scheduled Loads': 'NEM Registration and Exemption List.xls',
         'MNSP_INTERCONNECTOR': 'PUBLIC_DVD_MNSP_INTERCONNECTOR',
         'MNSP_PEROFFER': 'PUBLIC_DVD_MNSP_PEROFFER',
         'INTERCONNECTOR': 'PUBLIC_DVD_INTERCONNECTOR',
         'INTERCONNECTORCONSTRAINT': 'PUBLIC_DVD_INTERCONNECTORCONSTRAINT',
         'MNSP_DAYOFFER': 'PUBLIC_DVD_MNSP_DAYOFFER',
         'LOSSMODEL': 'PUBLIC_DVD_LOSSMODEL',
         'LOSSFACTORMODEL': 'PUBLIC_DVD_LOSSFACTORMODEL',
         'FCAS_4s_SCADA_MAP': '',
         'PLANTSTATS': '',
         'TRADINGLOAD': 'PUBLIC_DVD_TRADINGLOAD',
         'TRADINGPRICE': 'PUBLIC_DVD_TRADINGPRICE',
         'TRADINGREGIONSUM': 'PUBLIC_DVD_TRADINGREGIONSUM',
         'TRADINGINTERCONNECT': 'PUBLIC_DVD_TRADINGINTERCONNECT',
         'MARKET_PRICE_THRESHOLDS': 'PUBLIC_DVD_MARKET_PRICE_THRESHOLDS'}

table_types = {'FCAS Providers': 'STATICXL',
               'DISPATCHLOAD': 'MMS',
               'DUDETAILSUMMARY': 'MMS',
               'DUDETAIL': 'MMS',
               'DISPATCHCONSTRAINT': 'MMS',
               'GENCONDATA': 'MMS',
               'DISPATCH_UNIT_SCADA': 'MMS',
               'DISPATCHPRICE': 'MMS',
               'SPDREGIONCONSTRAINT': 'MMS',
               'SPDCONNECTIONPOINTCONSTRAINT': 'MMS',
               'SPDINTERCONNECTORCONSTRAINT': 'MMS',
               'BIDPEROFFER_D': 'MMS_AND_ARCHIVE',
               'DISPATCHINTERCONNECTORRES': 'MMS',
               'BIDDAYOFFER_D': 'MMS_AND_ARCHIVE',
               'DISPATCHREGIONSUM': 'MMS',
               'FCAS_4_SECOND': 'FCAS',
               'ELEMENTS_FCAS_4_SECOND': 'STATIC',
               'VARIABLES_FCAS_4_SECOND': 'STATIC',
               'Generators and Scheduled Loads': 'STATICXL',
               'MNSP_INTERCONNECTOR': 'MMS',
               'MNSP_PEROFFER': 'MMS',
               'INTERCONNECTOR': 'MMS',
               'INTERCONNECTORCONSTRAINT': 'MMS',
               'MNSP_DAYOFFER': 'MMS',
               'LOSSMODEL': 'MMS',
               'LOSSFACTORMODEL': 'MMS',
               'FCAS_4s_SCADA_MAP': 'CUSTOM',
               'TRADINGLOAD': 'MMS',
               'TRADINGPRICE': 'MMS',
               'TRADINGREGIONSUM': 'MMS',
               'TRADINGINTERCONNECT': 'MMS',
               'MARKET_PRICE_THRESHOLDS': 'MMS'
               }

dynamic_tables = [table for table, type in table_types.items() if type in ['MMS', 'MMS_AND_ARCHIVE', 'FCAS']]

return_tables = list(names.keys())

display_as_AMEO = ['FCAS Providers', 'DISPATCHLOAD', 'DUDETAILSUMMARY', 'DUDETAIL', 'DISPATCHCONSTRAINT', 'GENCONDATA', 'DISPATCH_UNIT_SCADA',
                   'DISPATCHPRICE', 'SPDREGIONCONSTRAINT', 'SPDCONNECTIONPOINTCONSTRAINT', 'SPDINTERCONNECTORCONSTRAINT',
                   'BIDPEROFFER_D', 'DISPATCHINTERCONNECTORRES', 'BIDDAYOFFER_D', 'DISPATCHREGIONSUM', 'FCAS_4_SECOND',
                   'ELEMENTS_FCAS_4_SECOND', 'VARIABLES_FCAS_4_SECOND', 'Generators and Scheduled Loads', 'TRADINGLOAD',
                   'TRADINGPRICE', 'TRADINGREGIONSUM', 'TRADINGINTERCONNECT']

display_as_Custom = ['FCAS_4s_SCADA_MAP', 'PLANTSTATS']

static_tables = ['ELEMENTS_FCAS_4_SECOND',
                 'VARIABLES_FCAS_4_SECOND',
                 'Generators and Scheduled Loads',
                 'FCAS Providers']

static_table_url = {
    'ELEMENTS_FCAS_4_SECOND': 'https://www.nemweb.com.au/Reports/Current/Causer_Pays_Elements/',
    'VARIABLES_FCAS_4_SECOND': 'https://aemo.com.au/-/media/files/electricity/nem/settlements_and_payments/settlements/auction-reports/archive/ancillary-services-market-causer-pays-variables-file.csv',
    'Generators and Scheduled Loads': 'https://www.aemo.com.au/-/media/Files/Electricity/NEM/Participant_Information/NEM-Registration-and-Exemption-List.xls',
    '_downloader.download_xl': 'https://www.aemo.com.au/-/media/Files/Electricity/NEM/Participant_Information/NEM-Registration-and-Exemption-List.xls'}

aemo_data_url = 'http://www.nemweb.com.au/Data_Archive/Wholesale_Electricity/MMSDM/{}/MMSDM_{}_{}/MMSDM_Historical_Data_SQLLoader/DATA/{}.zip'

fcas_4_url = 'http://www.nemweb.com.au/Reports/Current/Causer_Pays/FCAS_{}{}{}{}.zip'

fcas_4_url_hist = 'http://www.nemweb.com.au/Data_Archive/Wholesale_Electricity/FCAS_Causer_Pays/{}/FCAS_Causer_Pays_{}_{}/FCAS_{}{}{}{}.zip'

data_url = {'DISPATCHLOAD': 'aemo_data_url',
            'DUDETAILSUMMARY': 'aemo_data_url',
            'DUDETAIL': 'aemo_data_url',
            'DISPATCHCONSTRAINT': 'aemo_data_url',
            'GENCONDATA': 'aemo_data_url',
            'DISPATCH_UNIT_SCADA': 'aemo_data_url',
            'DISPATCHPRICE': 'aemo_data_url',
            'SPDREGIONCONSTRAINT': 'aemo_data_url',
            'SPDCONNECTIONPOINTCONSTRAINT': 'aemo_data_url',
            'SPDINTERCONNECTORCONSTRAINT': 'aemo_data_url',
            'BIDPEROFFER_D': 'aemo_data_url',
            'DISPATCHINTERCONNECTORRES': 'aemo_data_url',
            'INTERCONNECTOR': 'aemo_data_url',
            'INTERCONNECTORCONSTRAINT': 'aemo_data_url',
            'MNSP_INTERCONNECTOR': 'aemo_data_url',
            'BIDDAYOFFER_D': 'aemo_data_url',
            'DISPATCHREGIONSUM': 'aemo_data_url',
            'MNSP_DAYOFFER': 'aemo_data_url',
            'MNSP_PEROFFER': 'aemo_data_url',
            'LOSSMODEL': 'aemo_data_url',
            'LOSSFACTORMODEL': 'aemo_data_url',
            'DISPATCHCASESOLUTION': 'aemo_data_url',
            'FCAS': 'fcas_4_url',
            'TRADINGLOAD': 'aemo_data_url',
            'TRADINGPRICE': 'aemo_data_url',
            'TRADINGREGIONSUM': 'aemo_data_url',
            'TRADINGINTERCONNECT': 'aemo_data_url',
            'MARKET_PRICE_THRESHOLDS': 'aemo_data_url'
            }

filterable_cols = ['DUID', 'REGIONID', 'STATIONID', 'PARTICIPANTID', 'STARTTYPE', 'SCHEDULE_TYPE', 'GENCONID',
                   'BIDTYPE', 'VARIABLEID', 'INTERVENTION', 'DISPATCHMODE', 'STARTTYPE', 'CONNECTIONPOINTID',
                   'DISPATCHTYPE', 'CONSTRAINTID', 'PREDISPATCH', 'STPASA', 'MTPASA', 'LIMITTYPE', 'STATIONNAME',
                   'AGCFLAG', 'INTERCONNECTORID', 'NAME', 'Fuel Source - Primary', 'Fuel Source - Descriptor',
                   'Technology Type - Primary', 'Technology Type - Descriptor', 'ELEMENTNUMBER', 'MARKETNAME',
                   'VARIABLENUMBER', 'VARIABLETYPE', 'MMSDESCRIPTOR', 'ELEMENTTYPE', 'Region', 'Max Cap (MW)',
                   'Min Enablement Level', 'Max Enablement Level', 'Max Lower Angle', 'Max Upper Angle',
                   'Bid Type']

table_columns = {

    'DISPATCHLOAD': ['SETTLEMENTDATE', 'DUID', 'INTERVENTION', 'DISPATCHMODE', 'AGCSTATUS', 'INITIALMW',
                     'TOTALCLEARED', 'RAMPDOWNRATE', 'RAMPUPRATE', 'LOWER5MIN', 'LOWER60SEC',
                     'LOWER6SEC', 'RAISE5MIN', 'RAISE60SEC', 'RAISE6SEC', 'LOWERREG', 'RAISEREG',
                     'SEMIDISPATCHCAP', 'AVAILABILITY', 'RAISEREGENABLEMENTMAX', 'RAISEREGENABLEMENTMIN',
                     'LOWERREGENABLEMENTMAX', 'LOWERREGENABLEMENTMIN'],

    'TRADINGLOAD': ['SETTLEMENTDATE', 'DUID', 'INITIALMW', 'TOTALCLEARED', 'RAMPDOWNRATE', 'RAMPUPRATE', 'LOWER5MIN',
                    'LOWER60SEC', 'LOWER6SEC', 'RAISE5MIN', 'RAISE60SEC', 'RAISE6SEC', 'LOWERREG', 'RAISEREG',
                    'SEMIDISPATCHCAP', 'AVAILABILITY'],

    'TRADINGPRICE': ['SETTLEMENTDATE', 'REGIONID', 'RRP', 'RAISE6SECRRP', 'RAISE60SECRRP',
                     'RAISE5MINRRP', 'RAISEREGRRP', 'LOWER6SECRRP', 'LOWER60SECRRP', 'LOWER5MINRRP', 'LOWERREGRRP', 'PRICE_STATUS'],

    'TRADINGREGIONSUM': ['SETTLEMENTDATE', 'REGIONID', 'TOTALDEMAND',
                         'AVAILABLEGENERATION', 'AVAILABLELOAD', 'DEMANDFORECAST', 'DISPATCHABLEGENERATION',
                         'DISPATCHABLELOAD', 'NETINTERCHANGE', 'EXCESSGENERATION', 'LOWER5MINLOCALDISPATCH',
                         'LOWER60SECLOCALDISPATCH', 'LOWER6SECLOCALDISPATCH', 'RAISE5MINLOCALDISPATCH',
                         'RAISE60SECLOCALDISPATCH', 'RAISE6SECLOCALDISPATCH', 'LOWERREGLOCALDISPATCH',
                         'RAISEREGLOCALDISPATCH', 'INITIALSUPPLY', 'CLEAREDSUPPLY', 'TOTALINTERMITTENTGENERATION',
                         'DEMAND_AND_NONSCHEDGEN', 'UIGF'],

    'TRADINGINTERCONNECT': ['SETTLEMENTDATE', 'INTERCONNECTORID', 'MWFLOW', 'METEREDMWFLOW', 'MWLOSSES'],

    'DUDETAILSUMMARY': ['DUID', 'START_DATE', 'END_DATE', 'DISPATCHTYPE', 'CONNECTIONPOINTID', 'REGIONID', 'STATIONID',
                        'PARTICIPANTID', 'LASTCHANGED', 'TRANSMISSIONLOSSFACTOR', 'STARTTYPE', 'DISTRIBUTIONLOSSFACTOR',
                        'SCHEDULE_TYPE', 'MAX_RAMP_RATE_UP', 'MAX_RAMP_RATE_DOWN'],

    'DISPATCHCONSTRAINT': ['SETTLEMENTDATE', 'RUNNO', 'CONSTRAINTID', 'INTERVENTION', 'RHS', 'MARGINALVALUE',
                           'VIOLATIONDEGREE', 'LASTCHANGED', 'GENCONID_EFFECTIVEDATE', 'GENCONID_VERSIONNO', 'LHS',
                           'DISPATCHINTERVAL'],

    'GENCONDATA': ['GENCONID', 'EFFECTIVEDATE', 'VERSIONNO', 'CONSTRAINTTYPE', 'CONSTRAINTVALUE', 'DESCRIPTION',
                   'GENERICCONSTRAINTWEIGHT', 'LASTCHANGED', 'DISPATCH', 'PREDISPATCH', 'STPASA', 'MTPASA',
                   'LIMITTYPE', 'REASON'],

    'DISPATCH_UNIT_SCADA': ['SETTLEMENTDATE', 'DUID', 'SCADAVALUE'],

    'DUDETAIL': ['EFFECTIVEDATE', 'DUID', 'VERSIONNO', 'CONNECTIONPOINTID', 'REGISTEREDCAPACITY', 'AGCCAPABILITY',
                 'DISPATCHTYPE', 'MAXCAPACITY', 'STARTTYPE', 'NORMALLYONFLAG', 'LASTCHANGED'],

    'DISPATCHPRICE': ['SETTLEMENTDATE', 'REGIONID', 'INTERVENTION', 'RRP', 'RAISE6SECRRP', 'RAISE60SECRRP',
                      'RAISE5MINRRP', 'RAISEREGRRP', 'LOWER6SECRRP', 'LOWER60SECRRP', 'LOWER5MINRRP', 'LOWERREGRRP',
                      'PRICE_STATUS'],

    'SPDREGIONCONSTRAINT': ['REGIONID', 'EFFECTIVEDATE', 'VERSIONNO', 'GENCONID', 'FACTOR', 'LASTCHANGED', 'BIDTYPE'],

    'SPDCONNECTIONPOINTCONSTRAINT': ['CONNECTIONPOINTID', 'EFFECTIVEDATE', 'VERSIONNO', 'GENCONID', 'FACTOR', 'BIDTYPE',
                                     'LASTCHANGED'],

    'SPDINTERCONNECTORCONSTRAINT': ['INTERCONNECTORID', 'EFFECTIVEDATE', 'VERSIONNO', 'GENCONID', 'FACTOR',
                                    'LASTCHANGED'],

    'BIDPEROFFER_D': ['DUID', 'BANDAVAIL1', 'BANDAVAIL2', 'BANDAVAIL3', 'BANDAVAIL4', 'BANDAVAIL5', 'BANDAVAIL6',
                      'BANDAVAIL7', 'BANDAVAIL8', 'BANDAVAIL9', 'BANDAVAIL10', 'MAXAVAIL', 'BIDTYPE', 'SETTLEMENTDATE',
                      'ENABLEMENTMIN', 'ENABLEMENTMAX', 'LOWBREAKPOINT',
                      'HIGHBREAKPOINT', 'INTERVAL_DATETIME', 'OFFERDATE'],

    'DISPATCHINTERCONNECTORRES': ['SETTLEMENTDATE', 'INTERCONNECTORID', 'DISPATCHINTERVAL', 'INTERVENTION', 'MWFLOW',
                                  'METEREDMWFLOW', 'MWLOSSES'],

    'INTERCONNECTOR': ['INTERCONNECTORID', 'REGIONFROM', 'REGIONTO', 'LASTCHANGED'],

    'INTERCONNECTORCONSTRAINT': ['INTERCONNECTORID', 'FROMREGIONLOSSSHARE', 'EFFECTIVEDATE', 'VERSIONNO',
                                 'LOSSCONSTANT', 'LOSSFLOWCOEFFICIENT', 'ICTYPE'],

    'MNSP_INTERCONNECTOR': ['INTERCONNECTORID', 'LINKID', 'FROMREGION', 'TOREGION', 'MAXCAPACITY', 'FROM_REGION_TLF',
                            'TO_REGION_TLF', 'LHSFACTOR', 'EFFECTIVEDATE', 'VERSIONNO'],

    'BIDDAYOFFER_D': ['SETTLEMENTDATE', 'DUID', 'BIDTYPE', 'OFFERDATE', 'VERSIONNO', 'PRICEBAND1', 'PRICEBAND2',
                      'PRICEBAND3', 'PRICEBAND4', 'PRICEBAND5', 'PRICEBAND6', 'PRICEBAND7', 'PRICEBAND8',
                      'PRICEBAND9', 'PRICEBAND10', 'T1', 'T2', 'T3', 'T4', 'MINIMUMLOAD'],


    'DISPATCHREGIONSUM': ['SETTLEMENTDATE', 'REGIONID', 'DISPATCHINTERVAL', 'INTERVENTION', 'TOTALDEMAND',
                          'AVAILABLEGENERATION', 'AVAILABLELOAD', 'DEMANDFORECAST', 'DISPATCHABLEGENERATION',
                          'DISPATCHABLELOAD', 'NETINTERCHANGE', 'EXCESSGENERATION', 'LOWER5MINLOCALDISPATCH',
                          'LOWER60SECLOCALDISPATCH', 'LOWER6SECLOCALDISPATCH', 'RAISE5MINLOCALDISPATCH',
                          'RAISE60SECLOCALDISPATCH', 'RAISE6SECLOCALDISPATCH', 'LOWERREGLOCALDISPATCH',
                          'RAISEREGLOCALDISPATCH', 'INITIALSUPPLY', 'CLEAREDSUPPLY', 'TOTALINTERMITTENTGENERATION',
                          'DEMAND_AND_NONSCHEDGEN', 'UIGF', 'SEMISCHEDULE_CLEAREDMW', 'SEMISCHEDULE_COMPLIANCEMW'],

    'MNSP_PEROFFER': ['SETTLEMENTDATE', 'OFFERDATE', 'VERSIONNO', 'PARTICIPANTID', 'LINKID', 'PERIODID',
                      'BANDAVAIL1', 'BANDAVAIL2', 'BANDAVAIL3', 'BANDAVAIL4', 'BANDAVAIL5', 'BANDAVAIL6',
                      'BANDAVAIL7', 'BANDAVAIL8', 'BANDAVAIL9', 'BANDAVAIL10'],

    'MNSP_DAYOFFER': ['SETTLEMENTDATE', 'OFFERDATE', 'VERSIONNO', 'PARTICIPANTID', 'LINKID', 'PERIODID',
                      'PRICEBAND1', 'PRICEBAND2', 'PRICEBAND3', 'PRICEBAND4', 'PRICEBAND5', 'PRICEBAND6',
                      'PRICEBAND7', 'PRICEBAND8', 'PRICEBAND9', 'PRICEBAND10'],

    'LOSSMODEL': ['EFFECTIVEDATE', 'VERSIONNO', 'INTERCONNECTORID', 'LOSSSEGMENT', 'MWBREAKPOINT'],

    'LOSSFACTORMODEL': ['EFFECTIVEDATE', 'VERSIONNO', 'INTERCONNECTORID', 'REGIONID', 'DEMANDCOEFFICIENT'],

    'DISPATCHCASESOLUTION': ['SETTLEMENTDATE', 'TOTALOBJECTIVE'],

    'FCAS_4_SECOND': ['TIMESTAMP', 'ELEMENTNUMBER', 'VARIABLENUMBER', 'VALUE', 'VALUEQUALITY'],

    'ELEMENTS_FCAS_4_SECOND': ['ELEMENTNUMBER', 'EMSNAME', 'ELEMENTTYPE', 'MMSDESCRIPTOR'],

    'VARIABLES_FCAS_4_SECOND': ['VARIABLENUMBER', 'VARIABLETYPE'],

    'Generators and Scheduled Loads': ['Participant', 'Station Name', 'Region', 'Dispatch Type', 'Category', 'Classification',
                                       'Fuel Source - Primary', 'Fuel Source - Descriptor', 'Technology Type - Primary',
                                       'Technology Type - Descriptor', 'Aggregation', 'DUID', 'Reg Cap (MW)'],

    'FCAS Providers': ['Participant', 'Station Name', 'Region', 'DUID', 'Bid Type', 'Max Cap (MW)',
                       'Min Enablement Level', 'Max Enablement Level', 'Max Lower Angle', 'Max Upper Angle'],

    'FCAS_4s_SCADA_MAP': ['ELEMENTNUMBER', 'MARKETNAME', 'ERROR'],

    'PLANTSTATS': ['Month', 'DUID', 'CapacityFactor', 'Volume', 'TRADING_VWAP', 'DISPATCH_VWAP',
                   'NodalPeakCapacityFactor', 'Nodal90thPercentileCapacityFactor'],

    'MARKET_PRICE_THRESHOLDS': ['EFFECTIVEDATE', 'VERSIONNO', 'VOLL', 'MARKETPRICEFLOOR']}

table_primary_keys = {'DISPATCHCONSTRAINT': ['CONSTRAINTID', 'GENCONID_EFFECTIVEDATE', 'GENCONID_VERSIONNO',
                                             'SETTLEMENTDATE', 'INTERVENTION'],
                      'DUDETAILSUMMARY': ['DUID', 'START_DATE', 'END_DATE'], 'STATION': ['STATIONID'],
                      'DUDETAIL': ['EFFECTIVEDATE', 'DUID', 'VERSIONNO'],
                      'SPDREGIONCONSTRAINT': ['EFFECTIVEDATE', 'GENCONID', 'REGIONID', 'VERSIONNO', 'BIDTYPE'],
                      'SPDCONNECTIONPOINTCONSTRAINT': ['EFFECTIVEDATE', 'GENCONID', 'CONNECTIONPOINTID', 'VERSIONNO',
                                                       'BIDTYPE'],
                      'SPDINTERCONNECTORCONSTRAINT': ['EFFECTIVEDATE', 'GENCONID', 'INTERCONNECTORID', 'VERSIONNO'],
                      'GENCONDATA': ['GENCONID', 'EFFECTIVEDATE', 'VERSIONNO'],
                      'MNSP_PEROFFER': ['SETTLEMENTDATE', 'OFFERDATE', 'VERSIONNO', 'PARTICIPANTID', 'LINKID', 'PERIODID'],
                      'MNSP_DAYOFFER': ['SETTLEMENTDATE', 'OFFERDATE', 'VERSIONNO', 'PARTICIPANTID', 'LINKID'],
                      'INTERCONNECTORCONSTRAINT': ['EFFECTIVEDATE', 'INTERCONNECTORID', 'VERSIONNO'],
                      'MNSP_INTERCONNECTOR': ['EFFECTIVEDATE', 'LINKID', 'VERSIONNO'],
                      'LOSSMODEL': ['EFFECTIVEDATE', 'INTERCONNECTORID', 'LOSSSEGMENT', 'VERSIONNO'],
                      'LOSSFACTORMODEL': ['EFFECTIVEDATE', 'INTERCONNECTORID', 'REGIONID', 'VERSIONNO'],
                      'BIDPEROFFER_D': ['BIDTYPE', 'DUID', 'OFFERDATE', 'INTERVAL_DATETIME', 'SETTLEMENTDATE'],
                      'DISPATCHINTERCONNECTORRES': ['DISPATCHINTERVAL', 'INTERCONNECTORID', 'INTERVENTION',
                                                    'SETTLEMENTDATE'],
                      'INTERCONNECTOR': ['INTERCONNECTORID'],
                      'DISPATCHPRICE': ['INTERVENTION', 'REGIONID', 'SETTLEMENTDATE'],
                      'BIDDAYOFFER_D': ['BIDTYPE', 'DUID', 'SETTLEMENTDATE'],
                      'DISPATCHREGIONSUM': ['DISPATCHINTERVAL', 'INTERVENTION', 'REGIONID', 'SETTLEMENTDATE'],
                      'DISPATCHLOAD': ['SETTLEMENTDATE', 'INTERVENTION', 'DUID'],
                      'DISPATCH_UNIT_SCADA': ['SETTLEMENTDATE', 'DUID'],
                      'FCAS_4_SECOND': ['TIMESTAMP', 'ELEMENTNUMBER', 'VARIABLENUMBER'],
                      'ELEMENTS_FCAS_4_SECOND': ['ELEMENTNUMBER'],
                      'VARIABLES_FCAS_4_SECOND': ['VARIABLENUMBER', 'VARIABLETYPE'],
                      'Generators and Scheduled Loads': ['DUID'],
                      'FCAS Providers': ['DUID', 'Bid Type'],
                      'FCAS_4s_SCADA_MAP': ['ELEMENTNUMBER', 'MARKETNAME'],
                      'TRADINGLOAD': ['SETTLEMENTDATE', 'DUID'],
                      'TRADINGPRICE': ['SETTLEMENTDATE', 'REGIONID'],
                      'TRADINGREGIONSUM': ['SETTLEMENTDATE', 'REGIONID'],
                      'TRADINGINTERCONNECT': ['SETTLEMENTDATE', 'INTERCONNECTORID'],
                      'PLANTSTATS': ['Month', 'DUID'],
                      'MARKET_PRICE_THRESHOLDS': ['EFFECTIVEDATE', 'VERSIONNO']}

effective_date_group_col = {'SPDREGIONCONSTRAINT': ['GENCONID'],
                            'SPDCONNECTIONPOINTCONSTRAINT': ['GENCONID'],
                            'SPDINTERCONNECTORCONSTRAINT': ['GENCONID'],
                            'GENCONDATA': ['GENCONID'],
                            'MNSP_INTERCONNECTOR': ['INTERCONNECTORID'],
                            'INTERCONNECTORCONSTRAINT': ['INTERCONNECTORID'],
                            'INTERCONNECTOR': ['INTERCONNECTORID'],
                            'LOSSMODEL': ['INTERCONNECTORID'],
                            'LOSSFACTORMODEL': ['INTERCONNECTORID'],
                            'DUDETAILSUMMARY': ['DUID'],
                            'MNSP_PEROFFER': ['LINKID'],
                            'MNSP_DAYOFFER': ['LINKID'],
                            'DUDETAIL': ['DUID'],
                            'MARKET_PRICE_THRESHOLDS': []}

primary_date_columns = {'DISPATCHLOAD': 'SETTLEMENTDATE',
                        'TRADINGLOAD': 'SETTLEMENTDATE',
                        'TRADINGPRICE': 'SETTLEMENTDATE',
                        'TRADINGREGIONSUM': 'SETTLEMENTDATE',
                        'TRADINGINTERCONNECT': 'SETTLEMENTDATE',
                        'DUDETAILSUMMARY': 'START_DATE',
                        'DUDETAIL': 'EFFECTIVEDATE',
                        'DISPATCHCONSTRAINT': 'SETTLEMENTDATE',
                        'GENCONDATA': 'EFFECTIVEDATE',
                        'DISPATCH_UNIT_SCADA': 'SETTLEMENTDATE',
                        'DISPATCHPRICE': 'SETTLEMENTDATE',
                        'SPDREGIONCONSTRAINT': 'EFFECTIVEDATE',
                        'SPDCONNECTIONPOINTCONSTRAINT': 'EFFECTIVEDATE',
                        'SPDINTERCONNECTORCONSTRAINT': 'EFFECTIVEDATE',
                        'BIDPEROFFER_D': 'INTERVAL_DATETIME',
                        'DISPATCHINTERCONNECTORRES': 'SETTLEMENTDATE',
                        'BIDDAYOFFER_D': 'SETTLEMENTDATE',
                        'DISPATCHREGIONSUM': 'SETTLEMENTDATE',
                        'FCAS_4_SECOND': 'TIMESTAMP',
                        'ELEMENTS_FCAS_4_SECOND': None,
                        'VARIABLES_FCAS_4_SECOND': None,
                        'Generators and Scheduled Loads': None,
                        'FCAS Providers': None,
                        'MNSP_INTERCONNECTOR': 'EFFECTIVEDATE',
                        'MNSP_PEROFFER': 'SETTLEMENTDATE',
                        'INTERCONNECTOR': 'LASTCHANGED',
                        'INTERCONNECTORCONSTRAINT': 'EFFECTIVEDATE',
                        'MNSP_DAYOFFER': 'SETTLEMENTDATE',
                        'LOSSMODEL': 'EFFECTIVEDATE',
                        'LOSSFACTORMODEL': 'EFFECTIVEDATE',
                        'FCAS_4s_SCADA_MAP': None,
                        'MARKET_PRICE_THRESHOLDS': 'EFFECTIVEDATE'}

reg_exemption_list_tabs = {'Generators and Scheduled Loads': 'Generators and Scheduled Loads',
                           'FCAS Providers': 'Ancillary Services'}

months = ['01', '02', '03', '04', '05',
          '06', '07', '08', '09', '10', '11', '12']

nem_data_model_start_time = '2009/07/01 00:00:00'


# GUI settings.
header_y_pad = 30
query_y_pad = (20, 0)
query_row_offset = 2
row_height = 6
names_internal_row = 1
table_list_internal_row = 1
start_time_label_internal_row = 2
start_time_internal_row = 3
end_time_label_internal_row = 4
end_time_internal_row = 5
plus_internal_row = 6
plus_merge_internal_row = 7
list_row_span = 5
list_column_span = 1
save_field_column_span = 3
standard_x_pad = (0, 10)
list_filter_row_span = 4
internal_filter_row = 2
delete_button_internal_row = 5
last_column = 100
join_type = ['inner', 'left', 'right']

# Testing settings
raw_data_cache = 'D:/nemosis_test_cache'
