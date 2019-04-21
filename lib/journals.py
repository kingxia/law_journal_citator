from enum import IntEnum

class Journal():
    def __init__(self, _id, name, short):
        self.id = _id
        self.name = name
        self.short = short

class Journals(IntEnum):
    ABA_J_LAB_EMP_L = 0
    ADMIN_L_REV = 1
    AIPLA_QJ = 2
    AKRON_INTELL_PROP_J = 3
    AKRON_L_REV = 4
    AKRON_TAX_J = 5
    ALA_CR_CL_L_REV = 6
    ALA_L_REV = 7
    ALASKA_L_REV = 8
    ALB_GOVT_L_REV = 9
    ALB_LJ_SCI_TECH = 10
    ALB_L_REV = 11
    AM_BANKR_INST_L_REV = 12
    AM_CRIM_L_REV = 13
    AM_J_COMP_L = 14
    AM_J_CRIM_L = 15
    AM_J_JURIS = 16
    AM_JL_MED = 17
    AM_J_LEGAL_HIST = 18
    AM_J_TRIAL_ADVOC = 19
    AM_REV_INTL_ARB = 20
    AM_U_INTL_L_REV = 21
    AM_U_J_GENDER_SOC_POLY_L = 22
    AM_U_L_REV = 23
    ANIMAL_L = 24
    ANN_SURV_INTL_COMP_L = 25
    ANTITRUST_LJ = 26
    APPALACHIAN_JL = 27
    ARIZ_J_INTL_COMP_L = 28
    ARIZ_L_REV = 29
    ARIZ_ST_LJ = 30
    ARK_L_REV = 31
    ASIAN_AM_LJ = 32
    AVE_MARIA_L_REV = 33
    BARRY_L_REV = 34
    BAYLOR_L_REV = 35
    BERKELEY_BUS_LJ = 36
    BERKELEY_J_AFRAM_L_POLY = 37
    BERKELEY_J_EMP_LAB_L = 38
    BERKELEY_J_GENDER_L_JUST = 39
    BERKELEY_LA_RAZA_LJ = 40
    BERKELEY_TECH_LJ = 41
    BC_ENVTL_AFF_L_REV = 42
    BC_INTL_COMP_L_REV = 43
    BC_JL_SOC_JUST = 44
    BC_L_REV = 45
    BU_INTL_LJ = 46
    BU_J_SCI_TECH_L = 47
    BU_L_REV = 48
    BU_PUB_INT_LJ = 49
    BYU_EDUC_LJ = 50
    BYU_J_PUB_L = 51
    BYU_L_REV = 52
    BROOK_J_CORP_FIN_COM_L = 53
    BROOK_J_INTL_L = 54
    BROOK_L_REV = 55
    BUDDHISM_L_SOCY = 56
    BUFF_ENVTL_LJ = 57
    BUFF_HUM_RTS_L_REV = 58
    BUFF_INTELL_PROP_LJ = 59
    BUFF_L_REV = 60
    BUFF_PUB_INTEREST_LJ = 61
    BUS_LAW = 62
    CAL_L_REV = 63
    CAL_W_INTL_LJ = 64
    CAL_W_L_REV = 65
    CAMPBELL_L_REV = 66
    CANUS_LJ = 67
    CAPE_TOWN_CONVENTION_J = 68
    CAP_U_L_REV = 69
    CARDOZO_ARTS_ENT_LJ = 70
    CARDOZO_J_CONFLICT_RESOL = 71
    CARDOZO_JL_GENDER = 72
    CARDOZO_L_REV = 73
    CASE_W_RES_J_INTL_L = 74
    CASE_W_RES_L_REV = 75
    CATH_U_L_REV = 76
    CHAP_L_REV = 77
    CHARLESTON_L_REV = 78
    CHI_J_INTL_L = 79
    CHICANOLATINO_L_REV = 80
    CLEV_ST_L_REV = 81
    CLINICAL_L_REV = 82
    COLO_NAT_RESOURCES_ENERGY_ENVTL_L = 83
    COLUM_BUS_L_REV = 84
    COLUM_HUM_RTS_L_REV = 85
    COLUM_J_ASIAN_L = 86
    COLUM_J_ENVTL_L = 87
    COLUM_J_EUR_L = 88
    COLUM_J_GENDER_L = 89
    COLUM_JL_SOC_PROBS = 90
    COLUM_JL_ARTS = 91
    COLUM_J_TRANSNATL_L = 92
    COLUM_L_REV = 93
    COMMLAW_CONSPECTUS = 94
    COMP_LAB_L_POLY_J = 95
    CONCORDIA_L_REV = 96
    CONN_INS_LJ = 97
    CONN_J_INTL_L = 98
    CONN_L_REV = 99
    CONN_PUB_INT_LJ = 100
    CONST_COMMENT = 101
    CORNELL_INTL_LJ = 102
    CORNELL_JL_PUB_POLY = 103
    CORNELL_L_REV = 104
    CREIGHTON_L_REV = 105
    CUMB_L_REV = 106
    CUNY_L_REV = 107
    DEL_J_CORP_L = 108
    DENV_J_INTLL_L_POLY = 109
    DENV_L_REV = 110
    DEPAUL_J_FOR_SOC_JUST = 111
    DEPAUL_J_ART_TECH_INTELL_PROP_L = 112
    DEPAUL_J_HEALTH_CARE_L = 113
    DEPAUL_L_REV = 114
    DICKINSON_L_REV = 115
    DRAKE_J_AGRI_L = 116
    DRAKE_L_REV = 117
    DREXEL_L_REV = 118
    DUKE_LJ = 119
    DUQ_BUS_LJ = 120
    DUQ_L_REV = 121
    ECOLOGY_LQ = 122
    ELDER_LJ = 123
    ELON_L_REV = 124
    EMORY_BANKR_DEV_J = 125
    EMORY_INTL_L_REV = 126
    EMORY_LJ = 127
    EM_RTS_EMP_POLY_J = 128
    ENTREPRENEURIAL_BUS_LJ = 129
    ENVTL_L = 130
    ENVTL_L_REP_NEWS_ANALYSIS = 131
    ENVTL_LAW = 132
    ENVIRONS = 133
    FAM_LQ = 134
    FAULKNER_L_REV = 135
    FED_COMM_LJ = 136
    FED_CTS_L_REV = 137
    FIRST_AMEND_L_REV = 138
    FIU_L_REV = 139
    FLA_AM_U_L_REV = 140
    FLA_COASTAL_L_REV = 141
    FLA_J_INTL_L = 142
    FLA_L_REV = 143
    FLA_ST_U_BUS_REV = 144
    FLA_ST_U_L_REV = 145
    FLA_TAX_REV = 146
    FORDHAM_ENVTL_L_REV = 147
    FORDHAM_INTELL_PROP_MEDIA_ENT_LJ = 148
    FORDHAM_INTL_LJ = 149
    FORDHAM_L_REV = 150
    FORDHAM_URB_LJ = 151
    FREEDOM_CENTER_J = 152
    GEO_MASON_L_REV = 153
    GEO_MASON_U_CR_LJ = 154
    GEO_WASH_INTL_L_REV = 155
    GEO_WASH_J_ENERGY_ENVTL_L = 156
    GEO_WASH_L_REV = 157
    GEO_ENVTL_L_REV = 158
    GEO_IMMIGR_LJ = 159
    GEO_J_GENDER_L = 160
    GEO_J_INTL_L = 161
    GEO_JL_PUB_POLY = 162
    GEO_JL_CRITICAL_RACE_PERSP = 163
    GEO_J_LEGAL_ETHICS = 164
    GEO_J_ON_POVERTY_L_POLY = 165
    GEO_LJ = 166
    GEO_LJ_ANN_REV_CRIM_PROC = 167
    GA_J_INTL_COMP_L = 168
    GA_L_REV = 169
    GA_ST_U_L_REV = 170
    GOLDEN_GATE_U_ENVTL_LJ = 171
    GOLDEN_GATE_U_L_REV = 172
    GONZ_L_REV = 173
    HAMLINE_L_REV = 174
    HARV_CRCL_L_REV = 175
    HARV_ENVTL_L_REV = 176
    HARV_HUM_RTS_J = 177
    HARV_INTL_LJ = 178
    HARV_JL_GENDER = 179
    HARV_JL_PUB_POLY = 180
    HARV_JL_TECH = 181
    HARV_J_ON_LEGIS = 182
    HARV_J_ON_RACIAL_ETHNIC_JUST = 183
    HARV_LATINX_L_REV = 184
    HARV_L_POLY_REV = 185
    HARV_L_REV = 186
    HARV_NEGOT_L_REV = 187
    HASTINGS_BUS_LJ = 188
    HASTINGS_CONST_LQ = 189
    HASTINGS_LJ = 190
    HEALTH_MATRIX = 191
    HOFSTRA_LAB_EMP_LJ = 192
    HOFSTRA_L_REV = 193
    HOUS_BUS_TAX_LJ = 194
    HOUS_J_HEALTH_L_POLY = 195
    HOUS_J_INTL_L = 196
    HOUS_L_REV = 197
    HOWARD_HUM_CIV_RTS_L_REV = 198
    HOW_LJ = 199
    IS_JL_POLY_FOR_INFO_SOCY = 200
    IDAHO_L_REV = 201
    IDEA = 202
    ILSA_J_INTL_COMP_L = 203
    IMPACT = 204
    IND_J_GLOBAL_LEGAL_STUD = 205
    IND_LJ = 206
    INDIGENOUS_PEOPLES_JL_CULTURE_RESIST = 207
    INTELL_PROP_TECH_LJ = 208
    INTERCULTURAL_HUM_L_REV = 209
    INTL_COMP_POLY_ETHICS_L_REV = 210
    INTL_COMP_LQ = 211
    INTL_LAW = 212
    IOWA_L_REV = 213
    ISSUES_IN_L_MED = 214
    JEFFREY_S_MOORAD_SPORTS_LJ = 215
    J_MARSHALL_J_INFO_TECH_PRIVACY_L = 216
    J_AFFORDABLE_HOUSING_COMMUN_DEV_L = 217
    J_AIR_L_COM = 218
    J_ANIMAL_L_ETHICS = 219
    J_APP_PRAC_PROCESS = 220
    J_BUS_SEC_L = 221
    J_BUS_TECH_L = 222
    J_BUS_ENTREPRENEURSHIP_L = 223
    J_CATH_LEGAL_STUD = 224
    J_CIV_RTS_ECON_DEV = 225
    J_CONTEMP_HEALTH_L_POLY = 226
    J_CONTEMP_LEGAL_ISSUES = 227
    J_CORP_L = 228
    J_CRIM_L_CRIMINOLOGY = 229
    J_DISP_RESOL = 230
    J_EMPIRICAL_LEGAL_STUD = 231
    J_ENVTL_L_LITIG = 232
    J_FOOD_L_POLY = 233
    J_GENDER_RACE_JUST = 234
    J_HEALTH_BIOMED_L = 235
    J_HEALTH_CARE_L_POLY = 236
    J_INTELL_PROP_L = 237
    J_INTL_AGING_L_POLY = 238
    J_INTL_BUS_L = 239
    J_INTL_ECON_L = 240
    J_INTL_MEDIA_ENT_L = 241
    J_LAND_USE_ENVTL_L = 242
    JL_COM = 243
    JL_ECON = 244
    JL_EDUC = 245
    JL_FAM_STUD = 246
    JL_POLY = 247
    JL_POL = 248
    JL_RELIG = 249
    JL_SOC_CHALLENGES = 250
    JL_SOC_CHANGE = 251
    JL_ECON_ORG = 252
    JL_ECON_POLY = 253
    JL_SOCY = 254
    J_LEGAL_EDUC = 255
    J_LEGAL_STUD = 256
    J_MAR_L_COM = 257
    J_MED_L = 258
    J_NATL_SEC_L_POLY = 259
    J_RACE_GENDER_POVERTY = 260
    J_S_LEGAL_HIST = 261
    J_SPACE_L = 262
    J_SUP_CT_HIST = 263
    J_TECH_L_POLY = 264
    J_COPYRIGHT_SOCY_USA = 265
    J_LEGAL_PROF = 266
    J_TRANSNATL_L_POLY = 267
    JURIMETRICS_J = 268
    KAN_JL_PUB_POLY = 269
    KY_J_EQUINE_AGRI_NAT_RESOURCES_L = 270
    KY_LJ = 271
    LAW_BUS_REV_AM = 272
    LAW_CONTEMP_PROBS = 273
    LAW_HIST_REV = 274
    LAW_INEQ = 275
    LAW_POLY = 276
    LAW_PSYCHOL_REV = 277
    LAW_SOC_INQUIRY = 278
    LAW_SOCY_REV = 279
    LAW_LIBR_J = 280
    LEGAL_COMM_RHETORIC_JAWLD = 281
    LEGAL_INFO_REV = 282
    LEGAL_REF_SERV_Q = 283
    LEGAL_WRITING = 284
    LEWIS_CLARK_L_REV = 285
    LIBERTY_U_L_REV = 286
    LA_L_REV = 287
    LSU_J_ENERGY_L_RESOURCES = 288
    LOY_CONSUMER_L_REV = 289
    LOY_J_PUB_INT_L = 290
    LOY_L_REV = 291
    LOY_MAR_LJ = 292
    LOY_LA_ENT_L_REV = 293
    LOY_LA_INTL_COMP_L_REV = 294
    LOY_LA_L_REV = 295
    LOY_U_CHI_INTL_L_REV = 296
    LOY_U_CHI_LJ = 297
    ME_L_REV = 298
    MARQ_BEN_SOC_WELFARE_L_REV = 299
    MARQ_INTELL_PROP_L_REV = 300
    MARQ_L_REV = 301
    MARQ_SPORTS_L_REV = 302
    MD_J_INTL_L = 303
    MD_L_REV = 304
    MCGEORGE_L_REV = 305
    MEDIA_L_POLY = 306
    MERCER_L_REV = 307
    MICH_J_ENVTL_ADMIN_L = 308
    MICH_J_GENDER_L = 309
    MICH_J_INTL_L = 310
    MICH_J_RACE_L = 311
    MICH_L_REV = 312
    MICH_ST_INTL_L_REV = 313
    MICH_ST_L_REV = 314
    MICH_TELECOMM_TECH_L_REV = 315
    MINN_J_INTL_L = 316
    MINN_J_L_SCI_TECH = 317
    MINN_L_REV = 318
    MISS_C_L_REV = 319
    MISS_LJ = 320
    MO_ENVTL_L_POLY_REV = 321
    MO_L_REV = 322
    MONT_L_REV = 323
    NATL_BLACK_LJ = 324
    NEB_L_REV = 325
    NEGOTIATION_J = 326
    NEV_LJ = 327
    NEW_CRIM_L_REV = 328
    NEW_ENG_J_INTL_COMP_L = 329
    NEW_ENG_L_REV = 330
    NYL_SCH_L_REV = 331
    NYU_ANN_SURV_AM_L = 332
    NYU_ENVTL_LJ = 333
    NYU_J_INTL_L_POL = 334
    NYU_J_L_BUS = 335
    NYU_JL_LIBERTY = 336
    NYU_J_LEGIS_PUB_POLY = 337
    NYU_L_REV = 338
    NYU_REV_L_SOC_CHANGE = 339
    NC_BANK_INST = 340
    NC_CENT_L_REV = 341
    NC_J_INTL_L = 342
    NC_JL_TECH = 343
    NC_L_REV = 344
    ND_L_REV = 345
    N_ILL_U_L_REV = 346
    N_KY_L_REV = 347
    NW_INTERDISC_L_REV = 348
    NW_J_INTL_L_BUS = 349
    NW_U_L_REV = 350
    NOTRE_DAME_JL_ETHICS_PUB_POLY = 351
    NOTRE_DAME_L_REV = 352
    NOVA_L_REV = 353
    OHIO_NU_L_REV = 354
    OHIO_ST_BUS_LJ = 355
    OHIO_ST_J_CRIM_L = 356
    OHIO_ST_J_ON_DISP_RESOL = 357
    OHIO_ST_LJ = 358
    OKLA_CITY_U_L_REV = 359
    OR_L_REV = 360
    OR_REV_INTL_L = 361
    PACE_ENVTL_L_REV = 362
    PACE_INTL_L_REV = 363
    PACE_L_REV = 364
    PAC_MCGEORGE_GLOBAL_BUS_DEV_LJ = 365
    PENN_ST_ENVTL_L_REV = 366
    PENN_ST_INTL_L_REV = 367
    PENN_ST_L_REV = 368
    PEPP_DISP_RESOL_LJ = 369
    PEPP_L_REV = 370
    PERSPECTIVES = 371
    PITT_J_ENVTL_L_PUB_HEALTH_L = 372
    PITT_TAX_REV = 373
    PSYCHOL_PUB_POLY_L = 374
    PUB_CONT_LJ = 375
    PUB_LAND_RESOURCES_L_REV = 376
    QUINNIPIAC_HEALTH_L = 377
    QUINNIPIAC_L_REV = 378
    QUINNIPIAC_PROB_LJ = 379
    REAL_PROP_TR_EST_LJ = 380
    REGENT_J_INTL_L = 381
    REGENT_J_L_PUB_POLY = 382
    REGENT_U_L_REV = 383
    RESEARCH_IN_L_ECON = 384
    REV_BANKING_FIN_L = 385
    REV_LITIG = 386
    RICH_J_GLOBAL_L_BUS = 387
    ROGER_WILLLIAMS_U_L_REV = 388
    RUTGERS_COMPUTER_TECH_LJ = 389
    RUTGERS_U_L_REV = 390
    RUTGERS_RACE_L_REV = 391
    ST_LOUIS_U_J_HEALTH_L_POLY = 392
    ST_LOUIS_U_LJ = 393
    ST_LOUIS_U_PUB_L_REV = 394
    SAN_DIEGO_INTL_LJ = 395
    SAN_DIEGO_L_REV = 396
    SAVANNAH_L_REV = 397
    SCHOLAR = 398
    SCRIBES_J_LEGAL_WRITING = 399
    SEATTLE_J_FOR_SOC_JUST = 400
    SEATTLE_U_L_REV = 401
    SETON_HALL_CIR_REV = 402
    SETON_HALL_L_REV = 403
    SETON_HALL_LEGIS_J = 404
    SMU_L_REV = 405
    SMU_SCI_TECH_L_REV = 406
    SC_J_INTL_L_BUS = 407
    SC_L_REV = 408
    SD_L_REV = 409
    S_TEX_L_REV = 410
    S_CAL_INTERDISC_LJ = 411
    S_CAL_L_REV = 412
    S_CAL_REV_L_SOC_JUST = 413
    S_ILL_U_LJ = 414
    SU_L_REV = 415
    SW_JL_TRADE_AMERICAS = 416
    SW_L_REV = 417
    SPORTS_LAW_J = 418
    ST_MARYS_J_LEGAL_MAL_ETHICS = 419
    ST_JOHNS_L_REV = 420
    ST_MARYS_LJ = 421
    ST_THOMAS_L_REV = 422
    STAN_ENVTL_LJ = 423
    STAN_J_CR_CL = 424
    STAN_J_COMPLEX_LITIG = 425
    STAN_J_INTL_L = 426
    STAN_JL_BUS_FIN = 427
    STAN_L_POLY_REV = 428
    STAN_L_REV = 429
    STETSON_L_REV = 430
    SUFFOLK_J_TRIAL_APP_ADVOC = 431
    SUFFOLK_TRANSNATL_L_REV = 432
    SUFFOLK_UL_REV = 433
    SUP_CT_ECON_REV = 434
    SUP_CT_REV = 435
    SYRACUSE_J_INTL_L_COM = 436
    SYRACUSE_L_REV = 437
    TAX_L_REV = 438
    TAX_LAW = 439
    TEMP_INTL_COMP_LJ = 440
    TEMP_J_SCI_TECH_ENVTL_L = 441
    TEMP_L_REV = 442
    TEMP_POL_CIV_RTS_L_REV = 443
    TENN_JL_POLY = 444
    TENN_L_REV = 445
    TEX_AM_L_REV = 446
    TEX_ENVTL_LJ = 447
    TEX_HISP_JL_POLY = 448
    TEX_INTELL_PROP_LJ = 449
    TEX_INTL_LJ = 450
    TEX_J_OIL_GAS_ENERGY_L = 451
    TEX_J_WOMEN_GENDER_L = 452
    TEX_J_CL_CR = 453
    TEX_L_REV = 454
    TEX_REV_ENT_SPORTS_L = 455
    TEX_REV_L_POL = 456
    TEX_TECH_L_REV = 457
    TEX_WESLEYAN_L_REV = 458
    T_JEFFERSON_L_REV = 459
    T_MARSHALL_L_REV = 460
    TOURO_L_REV = 461
    TRANSACTIONS = 462
    TRANSNATL_L_CONTEMP_PROBS = 463
    TRANSP_LJ = 464
    TUL_ENVTL_LJ = 465
    TUL_EUR_CIV_LF = 466
    TUL_J_INTL_COMP_L = 467
    TUL_JL_SEXUALITY = 468
    TUL_J_TECH_INTELL_PROP = 469
    TUL_L_REV = 470
    TUL_MAR_LJ = 471
    TULSA_L_REV = 472
    UC_DAVIS_BUS_LJ = 473
    UC_DAVIS_J_INTL_L_POLY = 474
    UC_DAVIS_J_JUV_L_POLY = 475
    UC_DAVIS_L_REV = 476
    UC_IRVINE_L_REV = 477
    UCLA_ASIAN_PAC_AM_LJ = 478
    UCLA_J_ENVTL_L_AND_POLY = 479
    UCLA_J_INTL_L_FOREIGN_AFF = 480
    UCLA_J_ISLAMIC_NEAR_EL = 481
    UCLA_L_REV = 482
    UCLA_WOMENS_LJ = 483
    UMASS_L_REV = 484
    UMKC_L_REV = 485
    U_ARK_LITTLE_ROCK_L_REV = 486
    U_BALT_J_ENVTL_L = 487
    U_CHI_L_REV = 488
    U_CHI_L_SCH_ROUNDTABLE = 489
    U_CHI_LEGAL_F = 490
    U_CIN_L_REV = 491
    U_COLO_L_REV = 492
    U_DAYTON_L_REV = 493
    U_DENV_CRIM_L_REV = 494
    U_DENV_WATER_L_REV = 495
    U_DET_MERCY_L_REV = 496
    U_FLA_JL_PUB_POLY = 497
    U_HAW_L_REV = 498
    U_ILL_JL_TECH_POLY = 499
    U_ILL_L_REV = 500
    U_KAN_L_REV = 501
    U_LA_VERNE_L_REV = 502
    U_LOUISVILLE_L_REV = 503
    U_MD_LJ_RACE_RELIG_GENDER_CLASS = 504
    U_MEM_L_REV = 505
    U_MIAMI_BUS_L_REV = 506
    U_MIAMI_ENT_SPORTS_L_REV = 507
    U_MIAMI_INTERAM_L_REV = 508
    U_MIAMI_INTL_COMP_L_REV = 509
    U_MIAMI_L_REV = 510
    U_MICH_JL_REFORM = 511
    U_NH_L_REV = 512
    U_PA_J_BUS_L = 513
    U_PA_J_CONST_L = 514
    U_PA_J_INTL_L = 515
    U_PA_L_REV = 516
    U_PITT_L_REV = 517
    U_RICH_L_REV = 518
    USFL_REV = 519
    USF_MAR_LJ = 520
    U_ST_THOMAS_JL_PUB_POLY = 521
    U_ST_THOMAS_LJ = 522
    UDC_L_REV = 523
    U_TOL_L_REV = 524
    UNLV_GAMING_LJ = 525
    URB_LAW = 526
    UTAH_ENVTL_L_REV = 527
    UTAH_L_REV = 528
    VAL_U_L_REV = 529
    VAND_J_ENT_TECH_L = 530
    VAND_J_TRANSNATL_L = 531
    VAND_L_REV = 532
    VT_J_ENVTL_L = 533
    VT_L_REV = 534
    VILL_ENVTL_LJ = 535
    VILL_L_REV = 536
    VA_ENVTL_LJ = 537
    VA_J_CRIM_L = 538
    VA_J_INTL_L = 539
    VA_J_SOC_POLY_L = 540
    VA_L_BUS_REV = 541
    VA_L_REV = 542
    VA_SPORTS_ENT_LJ = 543
    VA_TAX_REV = 544
    WAKE_FOREST_JL_POLY = 545
    WAKE_FOREST_L_REV = 546
    WASHBURN_LJ = 547
    WASH_LEE_J_CR_SOC_JUST = 548
    WASH_LEE_L_REV = 549
    WASH_INTL_LJ = 550
    WASH_J_ENVTL_L_POLY = 551
    WASH_J_L_TECH_ARTS = 552
    WASH_L_REV = 553
    WASH_U_GLOBAL_STUD_L_REV = 554
    WASH_U_JL_POLY = 555
    WASH_U_JUR_REV = 556
    WASH_U_L_REV = 557
    WAYNE_L_REV = 558
    W_VA_L_REV = 559
    W_LEGAL_HIST = 560
    W_MICH_U_THOMAS_M_COOLEY_J_PRACTICAL_CLINICAL_L = 561
    W_MICH_U_THOMAS_M_COOLEY_L_REV = 562
    W_ST_L_REV = 563
    WHITTIER_J_CHILD_FAM_ADVOC = 564
    WHITTIER_L_REV = 565
    WIDENER_LJ = 566
    WIDENER_L_REVIEW = 567
    WILLAMETTE_J_INTL_L_DISP_RESOL = 568
    WILLAMETTE_L_REV = 569
    WM_MARY_BILL_RTS_J = 570
    WM_MARY_BUS_L_REV = 571
    WM_MARY_ENVTL_L_POLY_REV = 572
    WM_MARY_J_WOMEN_L = 573
    WM_MARY_L_REV = 574
    WM_MARY_POLY_REV = 575
    WM_MITCHELL_L_REV = 576
    WIS_INTL_LJ = 577
    WIS_JL_GENDER_SOC = 578
    WIS_L_REV = 579
    WIS_WOMENS_LJ = 580
    WOMENS_RTS_L_REP = 581
    WYO_L_REV = 582
    YALE_HUM_RTS_DEV_LJ = 583
    YALE_J_HEALTH_POLY_L_ETHICS = 584
    YALE_J_INTL_L = 585
    YALE_JL_FEMINISM = 586
    YALE_JL_HUMAN = 587
    YALE_J_ON_REG = 588
    YALE_L_POLY_REV = 589
    YALE_LJ = 590

JOURNALS = {
    0: Journal(0, 'ABA Journal of Labor & Employment Law', 'A.B.A. J. Lab. & Emp. L.'),
    1: Journal(1, 'Administrative Law Review', 'Admin. L. Rev.'),
    2: Journal(2, 'AIPLA Quarterly Journal', 'AIPLA Q.J.'),
    3: Journal(3, 'Akron Intellectual Property Journal', 'Akron Intell. Prop. J.'),
    4: Journal(4, 'Akron Law Review', 'Akron L. Rev.'),
    5: Journal(5, 'Akron Tax Journal', 'Akron Tax J.'),
    6: Journal(6, 'Alabama Civil Rights and Civil Liberties Law Review', 'Ala. C.R. & C.L. L. Rev.'),
    7: Journal(7, 'Alabama Law Review', 'Ala. L. Rev.'),
    8: Journal(8, 'Alaska Law Review', 'Alaska L. Rev.'),
    9: Journal(9, 'Albany Government Law Review', 'Alb. Gov\'t L. Rev.'),
    10: Journal(10, 'Albany Law Journal of Science & Technology', 'Alb. L.J. Sci. & Tech.'),
    11: Journal(11, 'Albany Law Review', 'Alb. L. Rev.'),
    12: Journal(12, 'American Bankruptcy Institute Law Review', 'Am. Bankr. Inst. L. Rev.'),
    13: Journal(13, 'American Criminal Law Review', 'Am. Crim. L. Rev.'),
    14: Journal(14, 'American Journal of Comparative Law', 'Am. J. Comp. L.'),
    15: Journal(15, 'American Journal of Criminal Law', 'Am. J. Crim. L.'),
    16: Journal(16, 'American Journal of Jurisprudence', 'Am. J. Juris.'),
    17: Journal(17, 'American Journal of Law & Medicine', 'Am. J.L. & Med.'),
    18: Journal(18, 'American Journal of Legal History', 'Am. J. Legal Hist.'),
    19: Journal(19, 'American Journal of Trial Advocacy', 'Am. J. Trial Advoc.'),
    20: Journal(20, 'American Review of International Arbitration', 'Am. Rev. Int\'l Arb.'),
    21: Journal(21, 'American University International Law Review', 'Am. U. Int\'l L. Rev.'),
    22: Journal(22, 'American University Journal of Gender, Social Policy & the Law', 'Am. U. J. Gender & Soc. Pol\'y & L.'),
    23: Journal(23, 'American University Law Review', 'Am. U. L. Rev.'),
    24: Journal(24, 'Animal Law', 'Animal L.'),
    25: Journal(25, 'Annual Survey of International & Comparative Law', 'Ann. Surv. Int\'l & Comp. L.'),
    26: Journal(26, 'Antitrust Law Journal', 'Antitrust L.J.'),
    27: Journal(27, 'Appalachian Journal of Law', 'Appalachian J.L.'),
    28: Journal(28, 'Arizona Journal of International and Comparative Law', 'Ariz. J. Int\'l & Comp. L.'),
    29: Journal(29, 'Arizona Law Review', 'Ariz. L. Rev.'),
    30: Journal(30, 'Arizona State Law Journal', 'Ariz. St. L.J.'),
    31: Journal(31, 'Arkansas Law Review', 'Ark. L. Rev.'),
    32: Journal(32, 'Asian American Law Journal', 'Asian Am.  L.J.'),
    33: Journal(33, 'Ave Maria Law Review', 'Ave Maria L. Rev.'),
    34: Journal(34, 'Barry Law Review', 'Barry L. Rev.'),
    35: Journal(35, 'Baylor Law Review', 'Baylor L. Rev.'),
    36: Journal(36, 'Berkeley Business Law Journal', 'Berkeley Bus. L.J.'),
    37: Journal(37, 'Berkeley Journal of African-American Law & Policy', 'Berkeley J. Afr.-Am. L. & Pol\'y'),
    38: Journal(38, 'Berkeley Journal of Employment and Labor Law', 'Berkeley J. Emp. & Lab. L.'),
    39: Journal(39, 'Berkeley Journal of Gender, Law & Justice', 'Berkeley J. Gender L. & Just.'),
    40: Journal(40, 'Berkeley La Raza Law Journal', 'Berkeley La Raza L.J.'),
    41: Journal(41, 'Berkeley Technology Law Journal', 'Berkeley Tech. L.J.'),
    42: Journal(42, 'Boston College Environmental Affairs Law Review', 'B.C. Envtl. Aff. L. Rev.'),
    43: Journal(43, 'Boston College International and Comparative Law Review', 'B.C. Int\'l & Comp. L. Rev.'),
    44: Journal(44, 'Boston College Journal of Law & Social Justice', 'B.C. J.L. & Soc. Just.'),
    45: Journal(45, 'Boston College Law Review', 'B.C. L. Rev.'),
    46: Journal(46, 'Boston University International Law Journal', 'B.U. Int\'l L.J.'),
    47: Journal(47, 'Boston University Journal of Science & Technology Law', 'B.U. J. Sci. & Tech. L.'),
    48: Journal(48, 'Boston University Law Review', 'B.U. L. Rev.'),
    49: Journal(49, 'Boston University Public Interest Law Journal', 'B.U. Pub. Int. L.J.'),
    50: Journal(50, 'Brigham Young University Education and Law Journal', 'BYU Educ. & L.J.'),
    51: Journal(51, 'Brigham Young University Journal of Public Law', 'BYU J. Pub. L.'),
    52: Journal(52, 'Brigham Young University Law Review', 'BYU L. Rev.'),
    53: Journal(53, 'Brooklyn Journal of Corporate, Financial & Commercial Law', 'Brook. J. Corp. Fin. & Com. L.'),
    54: Journal(54, 'Brooklyn Journal of International Law', 'Brook. J. Int\'l L.'),
    55: Journal(55, 'Brooklyn Law Review', 'Brook. L. Rev.'),
    56: Journal(56, 'Buddhism Law & Society', 'Buddhism L. & Soc\'y'),
    57: Journal(57, 'Buffalo Environmental Law Journal', 'Buff. Envtl. L.J.'),
    58: Journal(58, 'Buffalo Human Rights Law Review', 'Buff. Hum. Rts. L. Rev.'),
    59: Journal(59, 'Buffalo Intellectual Property Law Journal', 'Buff. Intell. Prop. L.J.'),
    60: Journal(60, 'Buffalo Law Review', 'Buff. L. Rev.'),
    61: Journal(61, 'Buffalo Public Interest Law Journal', 'Buff. Pub. Interest L.J.'),
    62: Journal(62, 'Business Lawyer', 'Bus. Law.'),
    63: Journal(63, 'California Law Review', 'Cal. L. Rev.'),
    64: Journal(64, 'California Western International Law Journal', 'Cal. W. Int\'l L.J.'),
    65: Journal(65, 'California Western Law Review', 'Cal. W. L. Rev.'),
    66: Journal(66, 'Campbell Law Review', 'Campbell L. Rev.'),
    67: Journal(67, 'Canada-United States Law Journal', 'Can.-U.S. L.J.'),
    68: Journal(68, 'Cape Town Convention Journal', 'Cape Town Convention J.'),
    69: Journal(69, 'Capital University Law Review', 'Cap. U. L. Rev.'),
    70: Journal(70, 'Cardozo Arts & Entertainment Law Journal', 'Cardozo Arts & Ent. L.J.'),
    71: Journal(71, 'Cardozo Journal of Conflict Resolution', 'Cardozo J. Conflict Resol.'),
    72: Journal(72, 'Cardozo Journal of Law & Gender', 'Cardozo J.L. & Gender'),
    73: Journal(73, 'Cardozo Law Review', 'Cardozo L. Rev.'),
    74: Journal(74, 'Case Western Reserve Journal of International Law', 'Case W. Res. J. Int\'l L.'),
    75: Journal(75, 'Case Western Reserve Law Review', 'Case W. Res. L. Rev.'),
    76: Journal(76, 'Catholic University Law Review', 'Cath. U. L. Rev.'),
    77: Journal(77, 'Chapman Law Review', 'Chap. L. Rev.'),
    78: Journal(78, 'Charleston Law Review', 'Charleston L. Rev.'),
    79: Journal(79, 'Chicago Journal of International Law', 'Chi. J. Int\'l L.'),
    80: Journal(80, 'Chicano-Latino Law Review', 'Chicano-Latino L. Rev.'),
    81: Journal(81, 'Cleveland State Law Review', 'Clev. St. L. Rev.'),
    82: Journal(82, 'Clinical Law Review', 'Clinical L. Rev.'),
    83: Journal(83, 'Colorado Natural Resources, Energy & Environmental Law Review', 'Colo. Nat. Resources Energy & Envtl. L.'),
    84: Journal(84, 'Columbia Business Law Review', 'Colum. Bus. L. Rev.'),
    85: Journal(85, 'Columbia Human Rights Law Review', 'Colum. Hum. Rts. L. Rev.'),
    86: Journal(86, 'Columbia Journal of Asian Law', 'Colum. J. Asian L.'),
    87: Journal(87, 'Columbia Journal of Environmental Law', 'Colum. J. Envtl. L.'),
    88: Journal(88, 'Columbia Journal of European Law', 'Colum. J. Eur. L.'),
    89: Journal(89, 'Columbia Journal of Gender and Law', 'Colum. J. Gender & L.'),
    90: Journal(90, 'Columbia Journal of Law and Social Problems', 'Colum. J.L. & Soc. Probs.'),
    91: Journal(91, 'Columbia Journal of Law & the Arts', 'Colum. J.L. & Arts'),
    92: Journal(92, 'Columbia Journal of Transnational Law', 'Colum. J. Transnat\'l L.'),
    93: Journal(93, 'Columbia Law Review', 'Colum. L. Rev.'),
    94: Journal(94, 'CommLaw Conspectus: Journal of Communications Law and Policy', 'CommLaw Conspectus'),
    95: Journal(95, 'Comparative Labor Law & Policy Journal', 'Comp. Lab. L. & Pol\'y J.'),
    96: Journal(96, 'Concordia Law Review', 'Concordia L. Rev.'),
    97: Journal(97, 'Connecticut Insurance Law Journal', 'Conn. Ins. L.J.'),
    98: Journal(98, 'Connecticut Journal of International Law', 'Conn. J. Int\'l L.'),
    99: Journal(99, 'Connecticut Law Review', 'Conn. L. Rev.'),
    100: Journal(100, 'Connecticut Public Interest Law Journal', 'Conn. Pub. Int. L.J.'),
    101: Journal(101, 'Constitutional Commentary', 'Const. Comment.'),
    102: Journal(102, 'Cornell International Law Journal', 'Cornell Int\'l L.J.'),
    103: Journal(103, 'Cornell Journal of Law and Public Policy', 'Cornell J.L. & Pub. Pol\'y'),
    104: Journal(104, 'Cornell Law Review', 'Cornell L. Rev.'),
    105: Journal(105, 'Creighton Law Review', 'Creighton L. Rev.'),
    106: Journal(106, 'Cumberland Law Review', 'Cumb. L. Rev.'),
    107: Journal(107, 'CUNY Law Review', 'CUNY L. Rev.'),
    108: Journal(108, 'Delaware Journal of Corporate Law', 'Del. J. Corp. L.'),
    109: Journal(109, 'Denver Journal of International Law and Policy', 'Denv. J. Intl\'l L. & Pol\'y'),
    110: Journal(110, 'Denver Law Review', 'Denv. L. Rev.'),
    111: Journal(111, 'DePaul Journal for Social Justice', 'DePaul J. for Soc. Just.'),
    112: Journal(112, 'DePaul Journal of Art, Technology & Intellectual Property Law', 'DePaul J. Art, Tech. & Intell. Prop. L.'),
    113: Journal(113, 'DePaul Journal of Health Care Law', 'DePaul J. Health Care L.'),
    114: Journal(114, 'DePaul Law Review', 'DePaul L. Rev.'),
    115: Journal(115, 'Dickinson Law Review', 'Dickinson L. Rev.'),
    116: Journal(116, 'Drake Journal of Agricultural Law', 'Drake J. Agri. L.'),
    117: Journal(117, 'Drake Law Review', 'Drake L. Rev.'),
    118: Journal(118, 'Drexel Law Review', 'Drexel L. Rev.'),
    119: Journal(119, 'Duke Law Journal', 'Duke L.J.'),
    120: Journal(120, 'Duquesne Business Law Journal', 'Duq. Bus. L.J.'),
    121: Journal(121, 'Duquesne Law Review', 'Duq. L. Rev.'),
    122: Journal(122, 'Ecology Law Quarterly', 'Ecology L.Q.'),
    123: Journal(123, 'Elder Law Journal', 'Elder L.J.'),
    124: Journal(124, 'Elon Law Review', 'Elon L. Rev.'),
    125: Journal(125, 'Emory Bankruptcy Developments Journal', 'Emory Bankr. Dev. J.'),
    126: Journal(126, 'Emory International Law Review', 'Emory Int\'l L. Rev.'),
    127: Journal(127, 'Emory Law Journal', 'Emory L.J.'),
    128: Journal(128, 'Employee Rights and Employment Policy Journal', 'Em. Rts. & Emp. Pol\'y J.'),
    129: Journal(129, 'Entrepreneurial Business Law Journal', 'Entrepreneurial Bus. L.J.'),
    130: Journal(130, 'Environmental Law', 'Envtl. L.'),
    131: Journal(131, 'Environmental Law Reporter News & Analysis', 'Envtl. L. Rep. News & Analysis'),
    132: Journal(132, 'Environmental Lawyer', 'Envtl. Law.'),
    133: Journal(133, 'Environs', 'Environs'),
    134: Journal(134, 'Family Law Quarterly', 'Fam. L.Q.'),
    135: Journal(135, 'Faulkner Law Review', 'Faulkner L. Rev.'),
    136: Journal(136, 'Federal Communications Law Journal', 'Fed. Comm. L.J.'),
    137: Journal(137, 'Federal Courts Law Review', 'Fed. Cts. L. Rev.'),
    138: Journal(138, 'First Amendment Law Review', 'First Amend. L. Rev.'),
    139: Journal(139, 'FIU Law Review', 'FIU L. Rev.'),
    140: Journal(140, 'Florida A&M University Law Review', 'Fla. A&M U. L. Rev.'),
    141: Journal(141, 'Florida Coastal Law Review', 'Fla. Coastal L. Rev.'),
    142: Journal(142, 'Florida Journal of International Law', 'Fla. J. Int\'l L.'),
    143: Journal(143, 'Florida Law Review', 'Fla. L. Rev.'),
    144: Journal(144, 'Florida State University Business Review', 'Fla. St. U. Bus. Rev.'),
    145: Journal(145, 'Florida State University Law Review', 'Fla. St. U. L. Rev.'),
    146: Journal(146, 'Florida Tax Review', 'Fla. Tax Rev.'),
    147: Journal(147, 'Fordham Environmental Law Review', 'Fordham Envtl. L. Rev.'),
    148: Journal(148, 'Fordham Intellectual Property, Media & Entertainment Law Journal', 'Fordham Intell. Prop. Media & Ent. L.J.'),
    149: Journal(149, 'Fordham International Law Journal', 'Fordham Int\'l L.J.'),
    150: Journal(150, 'Fordham Law Review', 'Fordham L. Rev.'),
    151: Journal(151, 'Fordham Urban Law Journal', 'Fordham Urb. L.J.'),
    152: Journal(152, 'Freedom Center Journal', 'Freedom Center J.'),
    153: Journal(153, 'George Mason Law Review', 'Geo. Mason L. Rev.'),
    154: Journal(154, 'George Mason University Civil Rights Law Journal', 'Geo. Mason U. C.R. L.J.'),
    155: Journal(155, 'George Washington International Law Review', 'Geo. Wash. Int\'l L. Rev.'),
    156: Journal(156, 'George Washington Journal of Energy and Environmental Law', 'Geo. Wash. J. Energy & Envtl. L.'),
    157: Journal(157, 'George Washington Law Review', 'Geo. Wash. L. Rev.'),
    158: Journal(158, 'Georgetown Environmental Law Review', 'Geo. Envtl. L. Rev.'),
    159: Journal(159, 'Georgetown Immigration Law Journal', 'Geo. Immigr. L.J.'),
    160: Journal(160, 'Georgetown Journal of Gender and the Law', 'Geo. J. Gender & L.'),
    161: Journal(161, 'Georgetown Journal of International Law', 'Geo. J. Int\'l L.'),
    162: Journal(162, 'Georgetown Journal of Law & Public Policy', 'Geo. J.L. & Pub. Pol\'y'),
    163: Journal(163, 'Georgetown Journal of Law & Modern Critical Race Perspectives', 'Geo. J.L. & Critical Race Persp.'),
    164: Journal(164, 'Georgetown Journal of Legal Ethics', 'Geo. J. Legal Ethics'),
    165: Journal(165, 'Georgetown Journal on Poverty Law & Policy', 'Geo. J. on Poverty L. & Pol\'y'),
    166: Journal(166, 'Georgetown Law Journal', 'Geo. L.J.'),
    167: Journal(167, 'Georgetown Law Journal Annual Review of Criminal Procedure', 'Geo. L.J. Ann. Rev. Crim. Proc.'),
    168: Journal(168, 'Georgia Journal of International and Comparative Law', 'Ga. J. Int\'l & Comp. L.'),
    169: Journal(169, 'Georgia Law Review', 'Ga. L. Rev.'),
    170: Journal(170, 'Georgia State University Law Review', 'Ga. St. U. L. Rev.'),
    171: Journal(171, 'Golden Gate University Environmental Law Journal', 'Golden Gate U. Envtl. L.J.'),
    172: Journal(172, 'Golden Gate University Law Review', 'Golden Gate U. L. Rev.'),
    173: Journal(173, 'Gonzaga Law Review', 'Gonz. L. Rev.'),
    174: Journal(174, 'Hamline Law Review', 'Hamline L. Rev.'),
    175: Journal(175, 'Harvard Civil Rights-Civil Liberties Law Review', 'Harv. C.R.-C.L. L. Rev.'),
    176: Journal(176, 'Harvard Environmental Law Review', 'Harv. Envtl. L. Rev.'),
    177: Journal(177, 'Harvard Human Rights Journal', 'Harv. Hum. Rts. J.'),
    178: Journal(178, 'Harvard International Law Journal', 'Harv. Int\'l L.J.'),
    179: Journal(179, 'Harvard Journal of Law & Gender', 'Harv. J.L. & Gender'),
    180: Journal(180, 'Harvard Journal of Law & Public Policy', 'Harv. J.L. & Pub. Pol\'y'),
    181: Journal(181, 'Harvard Journal of Law & Technology', 'Harv. J.L. & Tech.'),
    182: Journal(182, 'Harvard Journal on Legislation', 'Harv. J. on Legis.'),
    183: Journal(183, 'Harvard Journal on Racial & Ethnic Justice', 'Harv. J. on Racial & Ethnic Just.'),
    184: Journal(184, 'Harvard Latinx Law Review', 'Harv. Latinx L. Rev.'),
    185: Journal(185, 'Harvard Law & Policy Review', 'Harv. L. & Pol\'y Rev.'),
    186: Journal(186, 'Harvard Law Review', 'Harv. L. Rev.'),
    187: Journal(187, 'Harvard Negotiation Law Review', 'Harv. Negot. L. Rev.'),
    188: Journal(188, 'Hastings Business Law Journal', 'Hastings Bus. L.J.'),
    189: Journal(189, 'Hastings Constitutional Law Quarterly', 'Hastings Const. L.Q.'),
    190: Journal(190, 'Hastings Law Journal', 'Hastings L.J.'),
    191: Journal(191, 'Health Matrix', 'Health Matrix'),
    192: Journal(192, 'Hofstra Labor & Employment Law Journal', 'Hofstra Lab. & Emp. L.J.'),
    193: Journal(193, 'Hofstra Law Review', 'Hofstra L. Rev.'),
    194: Journal(194, 'Houston Business and Tax Law Journal', 'Hous. Bus. & Tax L.J.'),
    195: Journal(195, 'Houston Journal of Health Law & Policy', 'Hous. J. Health L. & Pol\'y'),
    196: Journal(196, 'Houston Journal of International Law', 'Hous. J. Int\'l L.'),
    197: Journal(197, 'Houston Law Review', 'Hous. L. Rev.'),
    198: Journal(198, 'Howard Human & Civil Rights Law Review', 'Howard Hum. & Civ. Rts. L. Rev.'),
    199: Journal(199, 'Howard Law Journal', 'How. L.J.'),
    200: Journal(200, 'I/S: A Journal of Law and Policy for the Information Society', 'I/S: J.L. & Pol\'y for Info. Soc\'y'),
    201: Journal(201, 'Idaho Law Review', 'Idaho L. Rev.'),
    202: Journal(202, 'IDEA', 'IDEA'),
    203: Journal(203, 'ILSA Journal of International and Comparative Law', 'ILSA J. Int\'l & Comp. L.'),
    204: Journal(204, 'IMPACT', 'IMPACT'),
    205: Journal(205, 'Indiana Journal of Global Legal Studies', 'Ind. J. Global Legal Stud.'),
    206: Journal(206, 'Indiana Law Journal', 'Ind. L.J.'),
    207: Journal(207, 'Indigenous Peoples\' Journal of Law, Culture & Resistance', 'Indigenous Peoples\' J.L. Culture & Resist.'),
    208: Journal(208, 'Intellectual Property and Technology Law Journal', 'Intell. Prop. & Tech. L.J.'),
    209: Journal(209, 'Intercultural Human Rights Law Review', 'Intercultural Hum. L. Rev.'),
    210: Journal(210, 'International Comparative, Policy & Ethics Law Review', 'Int\'l Comp., Pol\'y, & Ethics L. Rev.'),
    211: Journal(211, 'International and Comparative Law Quarterly', 'Int\'l & Comp. L.Q.'),
    212: Journal(212, 'International Lawyer', 'Int\'l Law.'),
    213: Journal(213, 'Iowa Law Review', 'Iowa L. Rev.'),
    214: Journal(214, 'Issues in Law & Medicine', 'Issues in L & Med.'),
    215: Journal(215, 'Jeffrey S. Moorad Sports Law Journal', 'Jeffrey S. Moorad Sports L.J.'),
    216: Journal(216, 'John Marshall Journal of Information Technology & Privacy Law', 'J. Marshall J. Info. Tech. & Privacy L.'),
    217: Journal(217, 'Journal of Affordable Housing & Community Development Law', 'J. Affordable Housing & Commun. Dev. L.'),
    218: Journal(218, 'Journal of Air Law and Commerce', 'J. Air L. & Com.'),
    219: Journal(219, 'Journal of Animal Law and Ethics', 'J. Animal L. & Ethics'),
    220: Journal(220, 'Journal of Appellate Practice and Process', 'J. App. Prac. & Process'),
    221: Journal(221, 'Journal of Business & Securities Law', 'J. Bus. & Sec. L.'),
    222: Journal(222, 'Journal of Business & Technology Law', 'J. Bus. & Tech. L.'),
    223: Journal(223, 'Journal of Business, Entrepreneurship & the Law', 'J. Bus. Entrepreneurship & L.'),
    224: Journal(224, 'Journal of Catholic Legal Studies', 'J. Cath. Legal Stud.'),
    225: Journal(225, 'Journal of Civil Rights and Economic Development', 'J. Civ. Rts. & Econ. Dev.'),
    226: Journal(226, 'Journal of Contemporary Health Law & Policy', 'J. Contemp. Health L. & Pol\'y'),
    227: Journal(227, 'Journal of Contemporary Legal Issues', 'J. Contemp. Legal Issues'),
    228: Journal(228, 'Journal of Corporation Law', 'J. Corp. L.'),
    229: Journal(229, 'Journal of Criminal Law and Criminology', 'J. Crim. L. & Criminology'),
    230: Journal(230, 'Journal of Dispute Resolution', 'J. Disp. Resol.'),
    231: Journal(231, 'Journal of Empirical Legal Studies', 'J. Empirical Legal Stud.'),
    232: Journal(232, 'Journal of Environmental Law and Litigation', 'J. Envtl. L. & Litig.'),
    233: Journal(233, 'Journal of Food Law & Policy', 'J. Food L. & Pol\'y'),
    234: Journal(234, 'Journal of Gender, Race and Justice', 'J. Gender Race & Just.'),
    235: Journal(235, 'Journal of Health & Biomedical Law', 'J. Health & Biomed. L.'),
    236: Journal(236, 'Journal of Health Care Law & Policy', 'J. Health Care L. & Pol\'y'),
    237: Journal(237, 'Journal of Intellectual Property Law', 'J. Intell. Prop. L.'),
    238: Journal(238, 'Journal of International Aging, Law & Policy', 'J. Int\'l Aging L. & Pol\'y'),
    239: Journal(239, 'Journal of International Business & Law', 'J. Int\'l Bus. & L.'),
    240: Journal(240, 'Journal of International Economic Law', 'J. Int\'l Econ. L.'),
    241: Journal(241, 'Journal of International Media & Entertainment Law', 'J. Int\'l Media & Ent. L.'),
    242: Journal(242, 'Journal of Land Use and Environmental Law', 'J. Land Use & Envtl. L.'),
    243: Journal(243, 'Journal of Law and Commerce', 'J.L. & Com.'),
    244: Journal(244, 'Journal of Law & Economics', 'J.L. & Econ.'),
    245: Journal(245, 'Journal of Law & Education', 'J.L. & Educ.'),
    246: Journal(246, 'Journal of Law & Family Studies', 'J.L. & Fam. Stud.'),
    247: Journal(247, 'Journal of Law and Policy', 'J.L. & Pol\'y'),
    248: Journal(248, 'Journal of Law and Politics', 'J.L. & Pol.'),
    249: Journal(249, 'Journal of Law and Religion', 'J.L. & Relig.'),
    250: Journal(250, 'Journal of Law & Social Challenges', 'J.L. & Soc. Challenges'),
    251: Journal(251, 'Journal of Law and Social Change', 'J.L. & Soc. Change'),
    252: Journal(252, 'Journal of Law, Economics & Organization', 'J.L. Econ. & Org.'),
    253: Journal(253, 'Journal of Law, Economics & Policy', 'J.L. Econ. & Pol\'y'),
    254: Journal(254, 'Journal of Law in Society', 'J.L. Soc\'y'),
    255: Journal(255, 'Journal of Legal Education', 'J. Legal Educ.'),
    256: Journal(256, 'Journal of Legal Studies', 'J. Legal Stud.'),
    257: Journal(257, 'Journal of Maritime Law and Commerce', 'J. Mar. L. & Com.'),
    258: Journal(258, 'Journal of Medicine and Law', 'J. Med. & L.'),
    259: Journal(259, 'Journal of National Security Law & Policy', 'J. Nat\'l Sec. L. & Pol\'y'),
    260: Journal(260, 'Journal of Race, Gender, and Poverty', 'J. Race, Gender & Poverty'),
    261: Journal(261, 'Journal of Southern Legal History', 'J. S. Legal Hist.'),
    262: Journal(262, 'Journal of Space Law', 'J. Space L.'),
    263: Journal(263, 'Journal of Supreme Court History', 'J. Sup. Ct. Hist.'),
    264: Journal(264, 'Journal of Technology Law & Policy', 'J. Tech. L. & Pol\'y'),
    265: Journal(265, 'Journal of the Copyright Society of the U.S.A.', 'J. Copyright Soc\'y U.S.A.'),
    266: Journal(266, 'Journal of the Legal Profession', 'J. Legal Prof.'),
    267: Journal(267, 'Journal of Transnational Law & Policy', 'J. Transnat\'l L. & Pol\'y'),
    268: Journal(268, 'Jurimetrics: The Journal of Law, Science, and Technology', 'Jurimetrics J.'),
    269: Journal(269, 'Kansas Journal of Law & Public Policy', 'Kan. J.L. & Pub. Pol\'y'),
    270: Journal(270, 'Kentucky Journal of Equine, Agriculture, and Natural Resources Law', 'Ky. J. Equine Agri. & Nat. Resources L.'),
    271: Journal(271, 'Kentucky Law Journal', 'Ky. L.J.'),
    272: Journal(272, 'Law and Business Review of the Americas', 'Law & Bus. Rev. Am.'),
    273: Journal(273, 'Law and Contemporary Problems', 'Law & Contemp. Probs.'),
    274: Journal(274, 'Law and History Review', 'Law & Hist. Rev.'),
    275: Journal(275, 'Law & Inequality', 'Law & Ineq.'),
    276: Journal(276, 'Law & Policy', 'Law & Pol\'y'),
    277: Journal(277, 'Law & Psychology Review', 'Law & Psychol. Rev.'),
    278: Journal(278, 'Law & Social Inquiry: Journal of the American Bar Foundation', 'Law & Soc. Inquiry'),
    279: Journal(279, 'Law & Society Review', 'Law & Soc\'y Rev.'),
    280: Journal(280, 'Law Library Journal', 'Law Libr. J.'),
    281: Journal(281, 'Legal Communication & Rhetoric: JALWD', 'Legal Comm. & Rhetoric: JAWLD'),
    282: Journal(282, 'Legal Information Review', 'Legal Info. Rev.'),
    283: Journal(283, 'Legal Reference Services Quarterly', 'Legal Ref. Serv. Q.'),
    284: Journal(284, 'Legal Writing: The Journal of the Legal Writing Institute', 'Legal Writing'),
    285: Journal(285, 'Lewis & Clark Law Review', 'Lewis & Clark L. Rev.'),
    286: Journal(286, 'Liberty University Law Review', 'Liberty U. L. Rev.'),
    287: Journal(287, 'Louisiana Law Review', 'La. L. Rev.'),
    288: Journal(288, 'Louisiana State University Journal of Energy Law and Resources', 'LSU J. Energy L. & Resources'),
    289: Journal(289, 'Loyola Consumer Law Review', 'Loy. Consumer L. Rev.'),
    290: Journal(290, 'Loyola Journal of Public Interest Law', 'Loy. J. Pub. Int. L.'),
    291: Journal(291, 'Loyola Law Review', 'Loy. L. Rev.'),
    292: Journal(292, 'Loyola Maritime Law Journal', 'Loy. Mar. L.J.'),
    293: Journal(293, 'Loyola of Los Angeles Entertainment Law Review', 'Loy. L.A. Ent. L. Rev.'),
    294: Journal(294, 'Loyola of Los Angeles International and Comparative Law Review', 'Loy. L.A. Int\'l & Comp. L. Rev.'),
    295: Journal(295, 'Loyola of Los Angeles Law Review', 'Loy. L.A. L. Rev.'),
    296: Journal(296, 'Loyola University Chicago International Law Review', 'Loy. U. Chi. Int\'l L. Rev.'),
    297: Journal(297, 'Loyola University Chicago Law Journal', 'Loy. U. Chi. L.J.'),
    298: Journal(298, 'Maine Law Review', 'Me. L. Rev.'),
    299: Journal(299, 'Marquette Benefits & Social Welfare Law Review', 'Marq. Ben. & Soc. Welfare L. Rev.'),
    300: Journal(300, 'Marquette Intellectual Property Law Review', 'Marq. Intell. Prop. L. Rev.'),
    301: Journal(301, 'Marquette Law Review', 'Marq. L. Rev.'),
    302: Journal(302, 'Marquette Sports Law Review', 'Marq. Sports L. Rev.'),
    303: Journal(303, 'Maryland Journal of International Law', 'Md. J. Int\'l L.'),
    304: Journal(304, 'Maryland Law Review', 'Md. L. Rev.'),
    305: Journal(305, 'McGeorge Law Review', 'McGeorge L. Rev.'),
    306: Journal(306, 'Media Law & Policy', 'Media L. & Pol\'y'),
    307: Journal(307, 'Mercer Law Review', 'Mercer L. Rev.'),
    308: Journal(308, 'Michigan Journal of Environmental & Administrative Law', 'Mich. J. Envtl. & Admin. L.'),
    309: Journal(309, 'Michigan Journal of Gender & Law', 'Mich. J. Gender & L.'),
    310: Journal(310, 'Michigan Journal of International Law', 'Mich. J. Int\'l L.'),
    311: Journal(311, 'Michigan Journal of Race & Law', 'Mich. J. Race & L.'),
    312: Journal(312, 'Michigan Law Review', 'Mich. L. Rev.'),
    313: Journal(313, 'Michigan State International Law Review', 'Mich. St. Int\'l L. Rev.'),
    314: Journal(314, 'Michigan State Law Review', 'Mich. St. L. Rev.'),
    315: Journal(315, 'Michigan Telecommunications and Technology Law Review', 'Mich. Telecomm. & Tech. L. Rev.'),
    316: Journal(316, 'Minnesota Journal of International Law', 'Minn. J. Int\'l L.'),
    317: Journal(317, 'Minnesota Journal of Law, Science & Technology', 'Minn. J. L. Sci. & Tech.'),
    318: Journal(318, 'Minnesota Law Review', 'Minn. L. Rev.'),
    319: Journal(319, 'Mississippi College Law Review', 'Miss. C. L. Rev.'),
    320: Journal(320, 'Mississippi Law Journal', 'Miss. L.J.'),
    321: Journal(321, 'Missouri Environmental Law and Policy Review', 'Mo. Envtl. L. & Pol\'y Rev.'),
    322: Journal(322, 'Missouri Law Review', 'Mo. L. Rev.'),
    323: Journal(323, 'Montana Law Review', 'Mont. L. Rev.'),
    324: Journal(324, 'National Black Law Journal', 'Nat\'l Black L.J.'),
    325: Journal(325, 'Nebraska Law Review', 'Neb. L. Rev.'),
    326: Journal(326, 'Negotiation Journal', 'Negotiation J.'),
    327: Journal(327, 'Nevada Law Journal', 'Nev. L.J.'),
    328: Journal(328, 'New Criminal Law Review', 'New Crim. L. Rev.'),
    329: Journal(329, 'New England Journal of International and Comparative Law', 'New Eng. J. Int\'l & Comp. L.'),
    330: Journal(330, 'New England Law Review', 'New Eng. L. Rev.'),
    331: Journal(331, 'New York Law School Law Review', 'N.Y.L. Sch. L. Rev.'),
    332: Journal(332, 'New York University Annual Survey of American Law', 'N.Y.U. Ann. Surv. Am. L.'),
    333: Journal(333, 'New York University Environmental Law Journal', 'N.Y.U. Envtl. L.J.'),
    334: Journal(334, 'New York University Journal of International Law and Politics', 'N.Y.U. J. Int\'l L. & Pol.'),
    335: Journal(335, 'New York University Journal of Law & Business', 'N.Y.U. J. L. & Bus.'),
    336: Journal(336, 'New York University Journal of Law & Liberty', 'N.Y.U. J.L. & Liberty'),
    337: Journal(337, 'New York University Journal of Legislation and Public Policy', 'N.Y.U. J. Legis. & Pub. Pol\'y'),
    338: Journal(338, 'New York University Law Review', 'N.Y.U. L. Rev.'),
    339: Journal(339, 'New York University Review of Law & Social Change', 'N.Y.U. Rev. L. & Soc. Change'),
    340: Journal(340, 'North Carolina Banking Institute', 'N.C. Bank. Inst.'),
    341: Journal(341, 'North Carolina Central Law Review', 'N.C. Cent. L. Rev.'),
    342: Journal(342, 'North Carolina Journal of International Law', 'N.C. J. Int\'l L.'),
    343: Journal(343, 'North Carolina Journal of Law & Technology', 'N.C. J.L. & Tech.'),
    344: Journal(344, 'North Carolina Law Review', 'N.C. L. Rev.'),
    345: Journal(345, 'North Dakota Law Review', 'N.D. L. Rev.'),
    346: Journal(346, 'Northern Illinois University Law Review', 'N. Ill. U. L. Rev.'),
    347: Journal(347, 'Northern Kentucky Law Review', 'N. Ky. L. Rev.'),
    348: Journal(348, 'Northwestern Interdisciplinary Law Review', 'Nw. Interdisc. L. Rev.'),
    349: Journal(349, 'Northwestern Journal of International Law & Business', 'Nw. J. Int\'l L. & Bus.'),
    350: Journal(350, 'Northwestern University Law Review', 'Nw. U. L. Rev.'),
    351: Journal(351, 'Notre Dame Journal of Law, Ethics & Public Policy', 'Notre Dame J.L. Ethics & Pub. Pol\'y'),
    352: Journal(352, 'Notre Dame Law Review', 'Notre Dame L. Rev.'),
    353: Journal(353, 'Nova Law Review', 'Nova L. Rev.'),
    354: Journal(354, 'Ohio Northern University Law Review', 'Ohio N.U. L. Rev.'),
    355: Journal(355, 'Ohio State Business Law Journal', 'Ohio St. Bus. L.J.'),
    356: Journal(356, 'Ohio State Journal of Criminal Law', 'Ohio St. J. Crim. L.'),
    357: Journal(357, 'Ohio State Journal on Dispute Resolution', 'Ohio St. J. on Disp. Resol.'),
    358: Journal(358, 'Ohio State Law Journal', 'Ohio St. L.J.'),
    359: Journal(359, 'Oklahoma City University Law Review', 'Okla. City U. L. Rev.'),
    360: Journal(360, 'Oregon Law Review', 'Or. L. Rev.'),
    361: Journal(361, 'Oregon Review of International Law', 'Or. Rev. Int\'l L.'),
    362: Journal(362, 'Pace Environmental Law Review', 'Pace Envtl. L. Rev.'),
    363: Journal(363, 'Pace International Law Review', 'Pace Int\'l L. Rev.'),
    364: Journal(364, 'Pace Law Review', 'Pace L. Rev.'),
    365: Journal(365, 'Pacific McGeorge Global Business & Development Law Journal', 'Pac. McGeorge Global Bus. & Dev. L.J.'),
    366: Journal(366, 'Penn State Environmental Law Review', 'Penn St. Envtl. L. Rev.'),
    367: Journal(367, 'Penn State International Law Review', 'Penn St. Int\'l L. Rev.'),
    368: Journal(368, 'Penn State Law Review', 'Penn St. L. Rev.'),
    369: Journal(369, 'Pepperdine Dispute Resolution Law Journal', 'Pepp. Disp. Resol. L.J.'),
    370: Journal(370, 'Pepperdine Law Review', 'Pepp. L. Rev.'),
    371: Journal(371, 'Perspectives: Teaching Legal Research and Writing', 'Perspectives'),
    372: Journal(372, 'Pittsburgh Journal of Environmental and Public Health Law', 'Pitt. J. Envtl. L. & Pub. Health L.'),
    373: Journal(373, 'Pittsburgh Tax Review', 'Pitt. Tax Rev.'),
    374: Journal(374, 'Psychology, Public Policy, and Law', 'Psychol. Pub. Pol\'y & L.'),
    375: Journal(375, 'Public Contract Law Journal', 'Pub. Cont. L.J.'),
    376: Journal(376, 'Public Land & Resources Law Review', 'Pub. Land & Resources L. Rev.'),
    377: Journal(377, 'Quinnipiac Health Law', 'Quinnipiac Health L.'),
    378: Journal(378, 'Quinnipiac Law Review (QLR)', 'Quinnipiac L. Rev.'),
    379: Journal(379, 'Quinnipiac Probate Law Journal', 'Quinnipiac Prob. L.J.'),
    380: Journal(380, 'Real Property, Trust and Estate Law Journal', 'Real Prop. Tr. & Est. L.J.'),
    381: Journal(381, 'Regent Journal of International Law', 'Regent J. Int\'l L.'),
    382: Journal(382, 'Regent Journal of Law & Public Policy', 'Regent J. L. & Pub. Pol\'y'),
    383: Journal(383, 'Regent University Law Review', 'Regent U. L. Rev.'),
    384: Journal(384, 'Research in Law and Economics', 'Research in L. & Econ.'),
    385: Journal(385, 'Review of Banking and Financial Law', 'Rev. Banking & Fin. L.'),
    386: Journal(386, 'Review of Litigation', 'Rev. Litig.'),
    387: Journal(387, 'Richmond Journal of Global Law and Business', 'Rich. J. Global L. & Bus.'),
    388: Journal(388, 'Roger Williams University Law Review', 'Roger Willliams U. L. Rev.'),
    389: Journal(389, 'Rutgers Computer and Technology Law Journal', 'Rutgers Computer & Tech. L.J.'),
    390: Journal(390, 'Rutgers University Law Review', 'Rutgers U. L. Rev.'),
    391: Journal(391, 'Rutgers Race and the Law Review', 'Rutgers Race & L. Rev.'),
    392: Journal(392, 'Saint Louis University Journal of Health Law & Policy', 'St. Louis U. J. Health L. & Pol\'y'),
    393: Journal(393, 'Saint Louis University Law Journal', 'St. Louis U. L.J.'),
    394: Journal(394, 'Saint Louis University Public Law Review', 'St. Louis U. Pub. L. Rev.'),
    395: Journal(395, 'San Diego International Law Journal', 'San Diego Int\'l L.J.'),
    396: Journal(396, 'San Diego Law Review', 'San Diego L. Rev.'),
    397: Journal(397, 'Savannah Law Review', 'Savannah L. Rev.'),
    398: Journal(398, 'Scholar: St. Mary\'s Law Review on Race and Social Justice', 'Scholar'),
    399: Journal(399, 'Scribes Journal of Legal Writing', 'Scribes J. Legal Writing'),
    400: Journal(400, 'Seattle Journal for Social Justice', 'Seattle J. for Soc. Just.'),
    401: Journal(401, 'Seattle University Law Review', 'Seattle U. L. Rev.'),
    402: Journal(402, 'Seton Hall Circuit Review', 'Seton Hall Cir. Rev.'),
    403: Journal(403, 'Seton Hall Law Review', 'Seton Hall L. Rev.'),
    404: Journal(404, 'Seton Hall Legislative Journal', 'Seton Hall Legis. J.'),
    405: Journal(405, 'SMU Law Review', 'SMU L. Rev.'),
    406: Journal(406, 'SMU Science and Technology Law Review', 'SMU Sci. & Tech. L. Rev.'),
    407: Journal(407, 'South Carolina Journal of International Law and Business', 'S.C. J. Int\'l L. & Bus.'),
    408: Journal(408, 'South Carolina Law Review', 'S.C. L. Rev.'),
    409: Journal(409, 'South Dakota Law Review', 'S.D. L. Rev.'),
    410: Journal(410, 'South Texas Law Review', 'S. Tex. L. Rev.'),
    411: Journal(411, 'Southern California Interdisciplinary Law Journal', 'S. Cal. Interdisc. L.J.'),
    412: Journal(412, 'Southern California Law Review', 'S. Cal. L. Rev.'),
    413: Journal(413, 'Southern California Review of Law and Social Justice', 'S. Cal. Rev. L. & Soc. Just.'),
    414: Journal(414, 'Southern Illinois University Law Journal', 'S. Ill. U. L.J.'),
    415: Journal(415, 'Southern University Law Review', 'S.U. L. Rev.'),
    416: Journal(416, 'Southwestern Journal of Law and Trade in the Americas', 'Sw. J.L. & Trade Americas'),
    417: Journal(417, 'Southwestern Law Review', 'Sw. L. Rev.'),
    418: Journal(418, 'Sports Lawyers Journal', 'Sports Law. J.'),
    419: Journal(419, 'St. Mary\'s Journal on Legal Malpractice & Ethics', 'St. Mary\'s J. Legal Mal. & Ethics'),
    420: Journal(420, 'St. John\'s Law Review', 'St. John\'s L. Rev.'),
    421: Journal(421, 'St. Mary\'s Law Journal', 'St. Mary\'s L.J.'),
    422: Journal(422, 'St. Thomas Law Review', 'St. Thomas L. Rev.'),
    423: Journal(423, 'Stanford Environmental Law Journal', 'Stan. Envtl. L.J.'),
    424: Journal(424, 'Stanford Journal of Civil Rights & Civil Liberties', 'Stan. J. C.R. & C.L.'),
    425: Journal(425, 'Stanford Journal of Complex Litigation', 'Stan. J. Complex Litig.'),
    426: Journal(426, 'Stanford Journal of International Law', 'Stan. J. Int\'l L.'),
    427: Journal(427, 'Stanford Journal of Law, Business & Finance', 'Stan. J.L. Bus. & Fin.'),
    428: Journal(428, 'Stanford Law & Policy Review', 'Stan. L. & Pol\'y Rev.'),
    429: Journal(429, 'Stanford Law Review', 'Stan. L. Rev.'),
    430: Journal(430, 'Stetson Law Review', 'Stetson L. Rev.'),
    431: Journal(431, 'Suffolk Journal of Trial & Appellate Advocacy', 'Suffolk J. Trial & App. Advoc.'),
    432: Journal(432, 'Suffolk Transnational Law Review', 'Suffolk Transnat\'l L. Rev.'),
    433: Journal(433, 'Suffolk University Law Review', 'Suffolk U.L. Rev.'),
    434: Journal(434, 'Supreme Court Economic Review', 'Sup. Ct. Econ. Rev.'),
    435: Journal(435, 'Supreme Court Review', 'Sup. Ct. Rev.'),
    436: Journal(436, 'Syracuse Journal of International Law and Commerce', 'Syracuse J. Int\'l L. & Com.'),
    437: Journal(437, 'Syracuse Law Review', 'Syracuse L. Rev.'),
    438: Journal(438, 'Tax Law Review', 'Tax L. Rev.'),
    439: Journal(439, 'Tax Lawyer', 'Tax Law.'),
    440: Journal(440, 'Temple International and Comparative Law Journal', 'Temp. Int\'l & Comp. L.J.'),
    441: Journal(441, 'Temple Journal of Science, Technology & Environmental Law', 'Temp. J. Sci. Tech. & Envtl. L.'),
    442: Journal(442, 'Temple Law Review', 'Temp. L. Rev.'),
    443: Journal(443, 'Temple Political & Civil Rights Law Review', 'Temp. Pol. & Civ. Rts. L. Rev.'),
    444: Journal(444, 'Tennessee Journal of Law & Policy', 'Tenn. J.L. & Pol\'y'),
    445: Journal(445, 'Tennessee Law Review', 'Tenn. L. Rev.'),
    446: Journal(446, 'Texas A&M Law Review', 'Tex. A&M L. Rev.'),
    447: Journal(447, 'Texas Environmental Law Journal', 'Tex. Envtl. L.J.'),
    448: Journal(448, 'Texas Hispanic Journal of Law & Policy', 'Tex. Hisp. J.L. & Pol\'y'),
    449: Journal(449, 'Texas Intellectual Property Law Journal', 'Tex. Intell. Prop. L.J.'),
    450: Journal(450, 'Texas International Law Journal', 'Tex. Int\'l L.J.'),
    451: Journal(451, 'Texas Journal of Oil, Gas, and Energy Law', 'Tex. J. Oil Gas & Energy L.'),
    452: Journal(452, 'Texas Journal of Women, Gender, and the Law', 'Tex. J. Women, Gender, & L.'),
    453: Journal(453, 'Texas Journal on Civil Liberties & Civil Rights', 'Tex. J. C.L. & C.R.'),
    454: Journal(454, 'Texas Law Review', 'Tex. L. Rev.'),
    455: Journal(455, 'Texas Review of Entertainment & Sports Law', 'Tex. Rev. Ent. & Sports L.'),
    456: Journal(456, 'Texas Review of Law & Politics', 'Tex. Rev. L. & Pol.'),
    457: Journal(457, 'Texas Tech Law Review', 'Tex. Tech L. Rev.'),
    458: Journal(458, 'Texas Wesleyan Law Review', 'Tex. Wesleyan L. Rev.'),
    459: Journal(459, 'Thomas Jefferson Law Review', 'T. Jefferson L. Rev.'),
    460: Journal(460, 'Thurgood Marshall Law Review', 'T. Marshall L. Rev.'),
    461: Journal(461, 'Touro Law Review', 'Touro L. Rev.'),
    462: Journal(462, 'Transactions: The Tennessee Journal of Business Law', 'Transactions'),
    463: Journal(463, 'Transnational Law & Contemporary Problems', 'Transnat\'l L. & Contemp. Probs.'),
    464: Journal(464, 'Transportation Law Journal', 'Transp. L.J.'),
    465: Journal(465, 'Tulane Environmental Law Journal', 'Tul. Envtl. L.J.'),
    466: Journal(466, 'Tulane European and Civil Law Forum', 'Tul. Eur. & Civ. L.F.'),
    467: Journal(467, 'Tulane Journal of International and Comparative Law', 'Tul. J. Int\'l & Comp. L.'),
    468: Journal(468, 'Tulane Journal of Law & Sexuality', 'Tul. J.L. & Sexuality'),
    469: Journal(469, 'Tulane Journal of Technology and Intellectual Property', 'Tul. J. Tech. & Intell. Prop.'),
    470: Journal(470, 'Tulane Law Review', 'Tul. L. Rev.'),
    471: Journal(471, 'Tulane Maritime Law Journal', 'Tul. Mar. L.J.'),
    472: Journal(472, 'Tulsa Law Review', 'Tulsa L. Rev.'),
    473: Journal(473, 'UC Davis Business Law Journal', 'U.C. Davis Bus. L.J.'),
    474: Journal(474, 'UC Davis Journal of International Law and Policy', 'UC Davis J. Int\'l L. & Pol\'y'),
    475: Journal(475, 'UC Davis Journal of Juvenile Law & Policy', 'U.C. Davis J. Juv. L. & Pol\'y'),
    476: Journal(476, 'U.C. Davis Law Review', 'U.C. Davis L. Rev.'),
    477: Journal(477, 'UC Irvine Law Review', 'UC Irvine L. Rev.'),
    478: Journal(478, 'UCLA Asian Pacific American Law Journal', 'UCLA Asian Pac. Am. L.J.'),
    479: Journal(479, 'UCLA Journal of Environmental Law & Policy', 'UCLA J. Envtl. L. and Pol\'y'),
    480: Journal(480, 'UCLA Journal of International Law and Foreign Affairs', 'UCLA J. Int\'l L. & Foreign Aff.'),
    481: Journal(481, 'UCLA Journal of Islamic and Near Eastern Law', 'UCLA J. Islamic & Near E.L.'),
    482: Journal(482, 'UCLA Law Review', 'UCLA L. Rev.'),
    483: Journal(483, 'UCLA Women\'s Law Journal', 'UCLA Women\'s L.J.'),
    484: Journal(484, 'UMass Law Review', 'UMass L. Rev.'),
    485: Journal(485, 'UMKC Law Review', 'UMKC L. Rev.'),
    486: Journal(486, 'University of Arkansas at Little Rock Law Review', 'U. Ark. Little Rock L. Rev.'),
    487: Journal(487, 'University of Baltimore Journal of Environmental Law', 'U. Balt. J. Envtl. L.'),
    488: Journal(488, 'University of Chicago Law Review', 'U. Chi. L. Rev.'),
    489: Journal(489, 'University of Chicago Law School Roundtable', 'U. Chi. L. Sch. Roundtable'),
    490: Journal(490, 'University of Chicago Legal Forum', 'U. Chi. Legal F.'),
    491: Journal(491, 'University of Cincinnati Law Review', 'U. Cin. L. Rev.'),
    492: Journal(492, 'University of Colorado Law Review', 'U. Colo. L. Rev.'),
    493: Journal(493, 'University of Dayton Law Review', 'U. Dayton L. Rev.'),
    494: Journal(494, 'University of Denver Criminal Law Review', 'U. Denv. Crim. L. Rev.'),
    495: Journal(495, 'University of Denver Water Law Review', 'U. Denv. Water L. Rev.'),
    496: Journal(496, 'University of Detroit Mercy Law Review', 'U. Det. Mercy L. Rev.'),
    497: Journal(497, 'University of Florida Journal of Law and Public Policy', 'U. Fla. J.L. & Pub. Pol\'y'),
    498: Journal(498, 'University of Hawaii Law Review', 'U. Haw. L. Rev.'),
    499: Journal(499, 'University of Illinois Journal of Law, Technology & Policy', 'U. Ill. J.L. Tech. & Pol\'y'),
    500: Journal(500, 'University of Illinois Law Review', 'U. Ill. L. Rev.'),
    501: Journal(501, 'University of Kansas Law Review', 'U. Kan. L. Rev.'),
    502: Journal(502, 'University of La Verne Law Review', 'U. La Verne L. Rev.'),
    503: Journal(503, 'University of Louisville Law Review', 'U. Louisville L. Rev.'),
    504: Journal(504, 'University of Maryland Law Journal of Race, Religion, Gender and Class', 'U. Md. L.J. Race Relig. Gender & Class'),
    505: Journal(505, 'University of Memphis Law Review', 'U. Mem. L. Rev.'),
    506: Journal(506, 'University of Miami Business Law Review', 'U. Miami Bus. L. Rev.'),
    507: Journal(507, 'University of Miami Entertainment & Sports Law Review', 'U. Miami Ent. & Sports L. Rev.'),
    508: Journal(508, 'University of Miami Inter-American Law Review', 'U. Miami Inter-Am. L. Rev.'),
    509: Journal(509, 'University of Miami International and Comparative Law Review', 'U. Miami Int\'l & Comp. L. Rev.'),
    510: Journal(510, 'University of Miami Law Review', 'U. Miami L. Rev.'),
    511: Journal(511, 'University of Michigan Journal of Law Reform', 'U. Mich. J.L. Reform'),
    512: Journal(512, 'University of New Hampshire Law Review', 'U. N.H. L. Rev.'),
    513: Journal(513, 'University of Pennsylvania Journal of Business Law', 'U. Pa. J. Bus. L.'),
    514: Journal(514, 'University of Pennsylvania Journal of Constitutional Law', 'U. Pa. J. Const. L.'),
    515: Journal(515, 'University of Pennsylvania Journal of International Law', 'U. Pa. J. Int\'l L.'),
    516: Journal(516, 'University of Pennsylvania Law Review', 'U. Pa. L. Rev.'),
    517: Journal(517, 'University of Pittsburgh Law Review', 'U. Pitt. L. Rev.'),
    518: Journal(518, 'University of Richmond Law Review', 'U. Rich. L. Rev.'),
    519: Journal(519, 'University of San Francisco Law Review', 'U.S.F.L. Rev.'),
    520: Journal(520, 'University of San Francisco Maritime Law Journal', 'U.S.F. Mar. L.J.'),
    521: Journal(521, 'University of St. Thomas Journal of Law & Public Policy', 'U. St. Thomas J.L. & Pub. Pol\'y'),
    522: Journal(522, 'University of St. Thomas Law Journal', 'U. St. Thomas L.J.'),
    523: Journal(523, 'University of the District of Columbia Law Review', 'U.D.C. L. Rev.'),
    524: Journal(524, 'University of Toledo Law Review', 'U. Tol. L. Rev.'),
    525: Journal(525, 'UNLV Gaming Law Journal', 'UNLV Gaming L.J.'),
    526: Journal(526, 'Urban Lawyer', 'Urb. Law.'),
    527: Journal(527, 'Utah Environmental Law Review', 'Utah Envtl. L. Rev.'),
    528: Journal(528, 'Utah Law Review', 'Utah L. Rev.'),
    529: Journal(529, 'Valparaiso University Law Review', 'Val. U. L. Rev.'),
    530: Journal(530, 'Vanderbilt Journal of Entertainment & Technology Law', 'Vand. J. Ent. & Tech. L.'),
    531: Journal(531, 'Vanderbilt Journal of Transnational Law', 'Vand. J. Transnat\'l L.'),
    532: Journal(532, 'Vanderbilt Law Review', 'Vand. L. Rev.'),
    533: Journal(533, 'Vermont Journal of Environmental Law', 'Vt. J. Envtl. L.'),
    534: Journal(534, 'Vermont Law Review', 'Vt. L. Rev.'),
    535: Journal(535, 'Villanova Environmental Law Journal', 'Vill. Envtl. L.J.'),
    536: Journal(536, 'Villanova Law Review', 'Vill. L. Rev.'),
    537: Journal(537, 'Virginia Environmental Law Journal', 'Va. Envtl. L.J.'),
    538: Journal(538, 'Virginia Journal of Criminal Law', 'Va. J. Crim. L.'),
    539: Journal(539, 'Virginia Journal of International Law', 'Va. J. Int\'l L.'),
    540: Journal(540, 'Virginia Journal of Social Policy & the Law', 'Va. J. Soc. Pol\'y & L.'),
    541: Journal(541, 'Virginia Law & Business Review', 'Va. L. & Bus. Rev.'),
    542: Journal(542, 'Virginia Law Review', 'Va. L. Rev.'),
    543: Journal(543, 'Virginia Sports and Entertainment Law Journal', 'Va. Sports & Ent. L.J.'),
    544: Journal(544, 'Virginia Tax Review', 'Va. Tax Rev.'),
    545: Journal(545, 'Wake Forest Journal of Law & Policy', 'Wake Forest J.L. & Pol\'y'),
    546: Journal(546, 'Wake Forest Law Review', 'Wake Forest L. Rev.'),
    547: Journal(547, 'Washburn Law Journal', 'Washburn L.J.'),
    548: Journal(548, 'Washington and Lee Journal of Civil Rights and Social Justice', 'Wash. & Lee. J. C.R. & Soc. Just.'),
    549: Journal(549, 'Washington and Lee Law Review', 'Wash. & Lee L. Rev.'),
    550: Journal(550, 'Washington International Law Journal', 'Wash. Int\'l L.J.'),
    551: Journal(551, 'Washington Journal of Environmental Law & Policy', 'Wash. J. Envtl. L. & Pol\'y'),
    552: Journal(552, 'Washington Journal of Law, Technology & Arts', 'Wash. J. L. Tech. & Arts'),
    553: Journal(553, 'Washington Law Review', 'Wash. L. Rev.'),
    554: Journal(554, 'Washington University Global Studies Law Review', 'Wash. U. Global Stud. L. Rev.'),
    555: Journal(555, 'Washington University Journal of Law & Policy', 'Wash. U. J.L. & Pol\'y'),
    556: Journal(556, 'Washington University Jurisprudence Review', 'Wash. U. Jur. Rev.'),
    557: Journal(557, 'Washington University Law Review', 'Wash. U. L. Rev.'),
    558: Journal(558, 'Wayne Law Review', 'Wayne L. Rev.'),
    559: Journal(559, 'West Virginia Law Review', 'W. Va. L. Rev.'),
    560: Journal(560, 'Western Legal History', 'W. Legal Hist.'),
    561: Journal(561, 'Western Michigan University Thomas M. Cooley Journal of Practical and Clinical Law', 'W. Mich. U. Thomas M. Cooley. J. Practical & Clinical L.'),
    562: Journal(562, 'Western Michigan University Thomas M. Cooley Law Review', 'W. Mich. U. Thomas M. Cooley L. Rev.'),
    563: Journal(563, 'Western State Law Review', 'W. St. L. Rev.'),
    564: Journal(564, 'Whittier Journal of Child and Family Advocacy', 'Whittier J. Child & Fam. Advoc.'),
    565: Journal(565, 'Whittier Law Review', 'Whittier L. Rev.'),
    566: Journal(566, 'Widener Law Journal', 'Widener L.J.'),
    567: Journal(567, 'Widener Law Review', 'Widener L. Review'),
    568: Journal(568, 'Willamette Journal of International Law and Dispute Resolution', 'Willamette J. Int\'l L. & Disp. Resol.'),
    569: Journal(569, 'Willamette Law Review', 'Willamette L. Rev.'),
    570: Journal(570, 'William & Mary Bill of Rights Journal', 'Wm. & Mary Bill Rts. J.'),
    571: Journal(571, 'William & Mary Business Law Review', 'Wm. & Mary Bus. L. Rev.'),
    572: Journal(572, 'William and Mary Environmental Law and Policy Review', 'Wm. & Mary Envtl. L. & Pol\'y Rev.'),
    573: Journal(573, 'William and Mary Journal of Women and the Law', 'Wm. & Mary J. Women & L.'),
    574: Journal(574, 'William and Mary Law Review', 'Wm. & Mary L. Rev.'),
    575: Journal(575, 'William & Mary Policy Review', 'Wm. & Mary Pol\'y Rev.'),
    576: Journal(576, 'William Mitchell Law Review', 'Wm. Mitchell L. Rev.'),
    577: Journal(577, 'Wisconsin International Law Journal', 'Wis. Int\'l L.J.'),
    578: Journal(578, 'Wisconsin Journal of Law, Gender & Society', 'Wis. J.L. Gender & Soc.'),
    579: Journal(579, 'Wisconsin Law Review', 'Wis. L. Rev.'),
    580: Journal(580, 'Wisconsin Women\'s Law Journal', 'Wis. Women\'s L.J.'),
    581: Journal(581, 'Women\'s Rights Law Reporter', 'Women\'s Rts. L. Rep.'),
    582: Journal(582, 'Wyoming Law Review', 'Wyo. L. Rev.'),
    583: Journal(583, 'Yale Human Rights & Development Law Journal', 'Yale Hum. Rts. & Dev. L.J.'),
    584: Journal(584, 'Yale Journal of Health, Policy, Law, and Ethics', 'Yale J. Health Pol\'y L. & Ethics'),
    585: Journal(585, 'Yale Journal of International Law', 'Yale J. Int\'l L.'),
    586: Journal(586, 'Yale Journal of Law and Feminism', 'Yale J.L. & Feminism'),
    587: Journal(587, 'Yale Journal of Law & the Humanities', 'Yale J.L. & Human.'),
    588: Journal(588, 'Yale Journal on Regulation', 'Yale J. on Reg.'),
    589: Journal(589, 'Yale Law & Policy Review', 'Yale L. & Pol\'y Rev.'),
    590: Journal(590, 'Yale Law Journal', 'Yale L.J.')
}