import numpy as np


def get_racing_line_waypoints():
    #waypoints will be inserted by the race line calc notebook
    return [[ 1.80577099, -3.94987297,  1.80577099, -3.41647291,  1.80577099,
        -4.48327303,  1.80577099, -3.94987297],
       [ 1.93577099, -3.94987297,  1.93577099, -3.41647291,  1.93577099,
        -4.48327303,  1.93577099, -3.94987297],
       [ 2.06577099, -3.94987297,  2.06577099, -3.41647291,  2.06577099,
        -4.48327303,  2.06577099, -3.94987297],
       [ 2.23728299, -3.94987297,  2.23728299, -3.41647291,  2.23728299,
        -4.48327303,  2.23728299, -3.94987297],
       [ 2.53879499, -3.94987297,  2.53879499, -3.41647291,  2.53879499,
        -4.48327303,  2.53879499, -3.94987297],
       [ 2.84030795, -3.94987297,  2.84030795, -3.41647291,  2.84030795,
        -4.48327303,  2.84030795, -3.94987297],
       [ 3.14181995, -3.94987297,  3.14181995, -3.41647291,  3.14181995,
        -4.48327303,  3.14181995, -3.94987297],
       [ 3.44333196, -3.94987297,  3.44333196, -3.41647291,  3.44333196,
        -4.48327303,  3.44333196, -3.94987297],
       [ 3.74484396, -3.94987297,  3.74484396, -3.41647291,  3.74484396,
        -4.48327303,  3.74484396, -3.94987297],
       [ 4.0463562 , -3.94987297,  4.0463562 , -3.41647291,  4.0463562 ,
        -4.48327303,  4.0463562 , -3.94987297],
       [ 4.34786797, -3.94987297,  4.34786797, -3.41647291,  4.34786797,
        -4.48327303,  4.34786797, -3.94987297],
       [ 4.64938116, -3.94987297,  4.64938116, -3.41647291,  4.64938116,
        -4.48327303,  4.64938116, -3.94987297],
       [ 4.95089293, -3.94987297,  4.95089293, -3.41647291,  4.95089293,
        -4.48327303,  4.94905463, -3.94704789],
       [ 5.25240517, -3.94987297,  5.25240517, -3.41647291,  5.25240517,
        -4.48327303,  5.24423188, -3.93743246],
       [ 5.55391693, -3.94987297,  5.55391693, -3.41647291,  5.55391693,
        -4.48327303,  5.53229233, -3.91739153],
       [ 5.85542917, -3.94987297,  5.85542917, -3.41647291,  5.85542917,
        -4.48327303,  5.81067094, -3.88365958],
       [ 6.15694189, -3.94987297,  6.15694189, -3.41647291,  6.15694189,
        -4.48327303,  6.07699095, -3.83352328],
       [ 6.45845413, -3.94987297,  6.45851707, -3.41647291,  6.45839119,
        -4.48327303,  6.32894093, -3.76463822],
       [ 6.75996494, -3.94994402,  6.75949812, -3.41654396,  6.76043177,
        -4.48334408,  6.56461209, -3.67543732],
       [ 7.06051898, -3.9493469 ,  6.96075296, -3.42535996,  7.160285  ,
        -4.47333384,  6.78017598, -3.56242972],
       [ 7.338902  , -3.83999145,  7.03218508, -3.40359712,  7.64561892,
        -4.27638578,  6.97171703, -3.42282701],
       [ 7.53574133, -3.61549008,  7.07256985, -3.35093808,  7.99891281,
        -3.88004208,  7.12909277, -3.24950323],
       [ 7.62964439, -3.33028746,  7.10678577, -3.22476792,  8.15250301,
        -3.43580699,  7.25581419, -3.05072311],
       [ 7.65377903, -3.03001952,  7.12115288, -3.00129008,  8.18640518,
        -3.05874896,  7.35264069, -2.83201161],
       [ 7.66209102, -2.72862446,  7.12880182, -2.71772289,  8.19538021,
        -2.73952603,  7.41976962, -2.59878356],
       [ 7.66610241, -2.42714143,  7.13271999, -2.42283893,  8.19948483,
        -2.43144393,  7.45772561, -2.35653485],
       [ 7.66695523, -2.12563145,  7.13355684, -2.12696099,  8.20035362,
        -2.12430191,  7.46718601, -2.11026817],
       [ 7.6645999 , -1.82413   ,  7.13123989, -1.83066404,  8.1979599 ,
        -1.81759596,  7.44927812, -1.86428387],
       [ 7.65956855, -1.52266055,  7.12628222, -1.53366005,  8.19285488,
        -1.51166105,  7.40554649, -1.6220322 ],
       [ 7.6521647 , -1.22123998,  7.11889315, -1.23294997,  8.18543625,
        -1.20953   ,  7.335369  , -1.38697254],
       [ 7.64633441, -0.91997406,  7.11852694, -0.99701142,  8.17414188,
        -0.84293669,  7.23839079, -1.16258853],
       [ 7.56627154, -0.63126908,  7.10032701, -0.89090627,  8.03221607,
        -0.37163189,  7.11188907, -0.95383485],
       [ 7.36332107, -0.41176399,  7.03661299, -0.83340043,  7.69002914,
         0.00987244,  6.94877239, -0.77030037],
       [ 7.09829187, -0.2690775 ,  6.87817192, -0.75494051,  7.31841183,
         0.21678551,  6.75798737, -0.60969851],
       [ 6.81604218, -0.16383712,  6.65504217, -0.67235923,  6.9770422 ,
         0.34468499,  6.54586928, -0.46863299],
       [ 6.52443409, -0.08740416,  6.40241003, -0.60665911,  6.64645815,
         0.43185079,  6.31679761, -0.34414843],
       [ 6.22927165, -0.02594769,  6.12954617, -0.54994237,  6.32899714,
         0.49804699,  6.07492888, -0.2327596 ],
       [ 5.93216014,  0.02531612,  5.84872818, -0.50151849,  6.0155921 ,
         0.55215073,  5.82431096, -0.1305876 ],
       [ 5.633744  ,  0.06836314,  5.5635252 , -0.46039471,  5.7039628 ,
         0.597121  ,  5.56922744, -0.03319474],
       [ 5.33443332,  0.10469438,  5.27497387, -0.42538121,  5.39389277,
         0.63476998,  5.30643479,  0.06943925],
       [ 5.03451085,  0.13558041,  4.98398876, -0.39542159,  5.08503294,
         0.66658241,  5.04436647,  0.17416401],
       [ 4.73414445,  0.16180901,  4.69166803, -0.3698971 ,  4.77662086,
         0.69351512,  4.78313642,  0.28118634],
       [ 4.43342304,  0.1835995 ,  4.3990612 , -0.3486926 ,  4.46778488,
         0.7158916 ,  4.52282558,  0.39061412],
       [ 4.13239336,  0.20065436,  4.07536983, -0.32968891,  4.18941689,
         0.73099762,  4.26354295,  0.50261679],
       [ 3.83513749,  0.2479015 ,  3.75064206, -0.27876359,  3.91963291,
         0.77456659,  4.00546328,  0.61749014],
       [ 3.53765452,  0.2960719 ,  3.37666297, -0.2124528 ,  3.69864607,
         0.8045966 ,  3.7487904 ,  0.73553031],
       [ 3.27034748,  0.426078  ,  2.98710704, -0.02590709,  3.55358791,
         0.87806308,  3.49369944,  0.85687496],
       [ 3.03417397,  0.61200259,  2.66601205,  0.22603311,  3.40233588,
         0.99797207,  3.24035263,  0.981529  ],
       [ 2.83678102,  0.83974646,  2.42651701,  0.49886689,  3.24704504,
         1.18062603,  2.98888853,  1.10936039],
       [ 2.64896953,  1.07561886,  2.23613811,  0.73785269,  3.06180096,
         1.41338503,  2.73933164,  1.24001398],
       [ 2.45497549,  1.30640513,  2.05540705,  0.9530493 ,  2.85454392,
         1.65976095,  2.4918853 ,  1.37336027],
       [ 2.249659  ,  1.52715302,  1.86891401,  1.15359104,  2.630404  ,
         1.90071499,  2.24682025,  1.50926238],
       [ 2.03284949,  1.73664647,  1.67147601,  1.34431398,  2.39422297,
         2.12897897,  2.00436142,  1.64749033],
       [ 1.80627745,  1.93554705,  1.46477401,  1.52580202,  2.1477809 ,
         2.34529209,  1.77298767,  1.7755986 ],
       [ 1.56997949,  2.1224345 ,  1.26302099,  1.68620896,  1.87693799,
         2.55866003,  1.54140686,  1.89075109],
       [ 1.31416148,  2.28182393,  1.05471897,  1.81577098,  1.57360399,
         2.74787688,  1.31004099,  1.98502412],
       [ 1.04394183,  2.41527152,  0.83780068,  1.92331505,  1.25008297,
         2.90722799,  1.08011289,  2.05140161],
       [ 0.75942415,  2.51428002,  0.63254499,  1.99618995,  0.88630331,
         3.03237009,  0.85366529,  2.08484096],
       [ 0.46180105,  2.55788052,  0.4715167 ,  2.02456903,  0.45208541,
         3.09119201,  0.63436551,  2.07756704],
       [ 0.16741552,  2.50373542,  0.38945389,  2.0187459 , -0.05462284,
         2.98872495,  0.42770499,  2.02265242],
       [-0.06505226,  2.31698108,  0.35144109,  1.98374104, -0.4815456 ,
         2.65022111,  0.24391962,  1.90926401],
       [-0.19711155,  2.04746401,  0.30843019,  1.87733698, -0.70265329,
         2.21759105,  0.07962829,  1.75843883],
       [-0.25503877,  1.75205553,  0.27200019,  1.66992402, -0.78207773,
         1.83418703, -0.06520079,  1.57620595],
       [-0.28980054,  1.45255703,  0.2405304 ,  1.395419  , -0.82013148,
         1.50969505, -0.19153765,  1.36812829],
       [-0.31963185,  1.15252697,  0.2115743 ,  1.10419798, -0.85083801,
         1.20085597, -0.30138448,  1.13955492],
       [-0.34443484,  0.85204092,  0.18740951,  0.81133211, -0.87627918,
         0.89274973, -0.39475416,  0.89352059],
       [-0.36565311,  0.55127743,  0.166669  ,  0.51738358, -0.89797521,
         0.58517128, -0.50611227,  0.66412809],
       [-0.3827517 ,  0.25025355,  0.1481085 ,  0.1982628 , -0.91361189,
         0.30224431, -0.63546192,  0.45202355],
       [-0.4242071 , -0.04712459,  0.07637922, -0.2313228 , -0.92479342,
         0.13707361, -0.78396544,  0.25917989],
       [-0.58477574, -0.29948138, -0.2109894 , -0.6800065 , -0.95856208,
         0.08104375, -0.95355134,  0.0888864 ],
       [-0.83994934, -0.45550886, -0.66476768, -0.95932132, -1.015131  ,
         0.0483036 , -1.15144132, -0.04682465],
       [-1.1379565 , -0.49158466, -1.08915806, -1.02274799, -1.18675494,
         0.03957867, -1.36997165, -0.15069736],
       [-1.43887097, -0.5104938 , -1.41242695, -1.04323804, -1.46531498,
         0.02225045, -1.60318054, -0.22296224],
       [-1.74017102, -0.5214773 , -1.73002899, -1.05478096, -1.75031304,
         0.01182636, -1.84484891, -0.26426406],
       [-2.04166698, -0.52195711, -2.05184197, -1.05525994, -2.03149199,
         0.01134572, -2.0893055 , -0.27546939],
       [-2.34291852, -0.50997771, -2.37729692, -1.04226899, -2.30854011,
         0.02231358, -2.33177441, -0.2585506 ],
       [-2.64319909, -0.48310734, -2.70709109, -1.01266694, -2.57930708,
         0.04645226, -2.5684512 , -0.21505723],
       [-2.94123244, -0.43779057, -3.04254794, -0.9614802 , -2.83991694,
         0.08589907, -2.7963782 , -0.14675693],
       [-3.23462093, -0.36869013, -3.3852489 , -0.88038027, -3.08399296,
         0.14300001, -3.01240275, -0.05389094],
       [-3.51856959, -0.26784305, -3.73597908, -0.75492489, -3.3011601 ,
         0.2192388 , -3.213093  ,  0.06354866],
       [-3.78305244, -0.12391561, -4.09011078, -0.56006992, -3.47599411,
         0.31223869, -3.39481   ,  0.20556837],
       [-4.00740743,  0.07624336, -4.42045784, -0.26125479, -3.59435701,
         0.4137415 , -3.55002653,  0.37538481],
       [-4.15858161,  0.33555375, -4.65780115,  0.14768299, -3.65936208,
         0.52342451, -3.66854883,  0.57534741],
       [-4.21591961,  0.63042405, -4.74848223,  0.60054529, -3.683357  ,
         0.66030282, -3.75748735,  0.79503894],
       [-4.19187856,  0.93042287, -4.71720219,  1.02289295, -3.66655493,
         0.83795279, -3.81942628,  1.03035132],
       [-4.11195207,  1.2208975 , -4.61793709,  1.38970101, -3.60596704,
         1.05209398, -3.85685316,  1.27819447],
       [-4.00138211,  1.50139403, -4.50150824,  1.68683803, -3.50125599,
         1.31595004, -3.87271975,  1.53593321],
       [-3.9023639 ,  1.78613496, -4.4110508 ,  1.94661295, -3.393677  ,
         1.62565696, -3.87017988,  1.80138883],
       [-3.82005584,  2.07616645, -4.33646679,  2.20971489, -3.3036449 ,
         1.94261801, -3.8523597 ,  2.07278503],
       [-3.75143957,  2.369735  , -4.27385902,  2.47740793, -3.22902012,
         2.26206207, -3.84628969,  2.33804538],
       [-3.698385  ,  2.66650653, -4.22614193,  2.743891  , -3.17062807,
         2.58912206, -3.8605756 ,  2.5926587 ],
       [-3.664011  ,  2.96598601, -4.19620991,  3.00175905, -3.1318121 ,
         2.93021297, -3.90105543,  2.83184369],
       [-3.65799844,  3.26726103, -4.19017696,  3.23118496, -3.12581992,
         3.3033371 , -3.97208252,  3.05019786],
       [-3.70451987,  3.56435156, -4.19883585,  3.36393404, -3.21020389,
         3.76476908, -4.07689383,  3.2411506 ],
       [-3.87529349,  3.8060801 , -4.21701002,  3.39651299, -3.53357697,
         4.21564722, -4.21705739,  3.39714606],
       [-4.14703918,  3.93232965, -4.28881311,  3.41811609, -4.00526524,
         4.44654322, -4.39684663,  3.50191864],
       [-4.4460206 ,  3.96327448, -4.43960524,  3.42991304, -4.45243597,
         4.49663591, -4.60271169,  3.56125313],
       [-4.74467182,  3.92508245, -4.6346488 ,  3.40315294, -4.85469484,
         4.44701195, -4.8270725 ,  3.57725873],
       [-5.03352618,  3.83941114, -4.8520112 ,  3.33784604, -5.21504116,
         4.34097624, -5.06345181,  3.55069506],
       [-5.31040645,  3.72033858, -5.078444  ,  3.24001694, -5.54236889,
         4.20066023, -5.3045569 ,  3.4833835 ],
       [-5.57586455,  3.57749605, -5.3074379 ,  3.11655903, -5.84429121,
         4.03843307, -5.54263052,  3.37959626],
       [-5.83112812,  3.41709507, -5.53516912,  2.97333407, -6.12708712,
         3.86085606, -5.77140112,  3.24545066],
       [-6.07731295,  3.24306297, -5.75962496,  2.81458902, -6.39500093,
         3.67153692, -5.98745875,  3.0873207 ],
       [-6.31537247,  3.058056  , -5.98024082,  2.6430831 , -6.65050411,
         3.4730289 , -6.18900416,  2.90968735],
       [-6.54634953,  2.8642695 , -6.19711685,  2.461092  , -6.8955822 ,
         3.26744699, -6.37566863,  2.71637141],
       [-6.77110648,  2.66329908, -6.4102211 ,  2.27051711, -7.13199186,
         3.05608106, -6.54785693,  2.51032525],
       [-6.99035096,  2.4563241 , -6.61965704,  2.07278609, -7.36104488,
         2.83986211, -6.70532715,  2.29312613],
       [-7.2046721 ,  2.24425244, -6.82560301,  1.86898994, -7.58374119,
         2.61951494, -6.84801973,  2.06612716],
       [-7.41456938,  2.02780157, -7.00524187,  1.68579805, -7.82389688,
         2.3698051 , -6.97531866,  1.83009486],
       [-7.58958673,  1.78369957, -7.10609913,  1.55841005, -8.07307434,
         2.0089891 , -7.08544027,  1.58519477],
       [-7.66369057,  1.49357104, -7.13210201,  1.44964504, -8.19527912,
         1.53749704, -7.16620003,  1.32849064],
       [-7.63809466,  1.19381446, -7.1102252 ,  1.27042496, -8.16596413,
         1.11720395, -7.22123282,  1.06500058],
       [-7.57728887,  0.89850816, -7.05220079,  0.99230862, -8.10237694,
         0.80470771, -7.25370357,  0.79817838],
       [-7.53211522,  0.6005744 , -7.00017691,  0.64003062, -8.06405354,
         0.56111819, -7.26700148,  0.53036994],
       [-7.53283739,  0.29949535, -7.00191879,  0.24810199, -8.06375599,
         0.3508887 , -7.26328214,  0.26303946],
       [-7.58987474,  0.0038804 , -7.06527615, -0.0926161 , -8.11447334,
         0.1003769 , -7.24413283, -0.00279503],
       [-7.64171576, -0.292399  , -7.1100421 , -0.33528289, -8.17338943,
        -0.2495151 , -7.21087076, -0.26641425],
       [-7.63802433, -0.59367305, -7.10589314, -0.55691111, -8.17015553,
        -0.63043499, -7.16461808, -0.52731153],
       [-7.60023713, -0.8927041 , -7.07449007, -0.80267322, -8.12598419,
        -0.98273498, -7.10612831, -0.7850628 ],
       [-7.53636909, -1.18729496, -7.01948309, -1.05559695, -8.05325508,
        -1.31899297, -7.03604976, -1.03931745],
       [-7.4514761 , -1.47655696, -6.94506502, -1.30903494, -7.95788717,
        -1.64407897, -6.95499472, -1.28980436],
       [-7.347121  , -1.75938249, -6.85325384, -1.55786002, -7.84098816,
        -1.96090496, -6.86210655, -1.53572369],
       [-7.22381783, -2.03447551, -6.74475479, -1.79992497, -7.70288086,
        -2.26902604, -6.75601309, -1.77588164],
       [-7.08214951, -2.30057895, -6.62054396, -2.03330398, -7.54375505,
        -2.56785393, -6.63402911, -2.00804122],
       [-6.92190003, -2.55591345, -6.48099709, -2.25571299, -7.36280298,
        -2.85611391, -6.49682263, -2.23135844],
       [-6.74306703, -2.79858851, -6.32666492, -2.46523499, -7.15946913,
        -3.13194203, -6.34315049, -2.44372637],
       [-6.54541707, -3.02618992, -6.15819216, -2.65934896, -6.93264198,
        -3.39303088, -6.17246949, -2.64309647],
       [-6.32883763, -3.23583603, -5.97620106, -2.83563209, -6.68147421,
        -3.63603997, -5.98484913, -2.82765657],
       [-6.0936079 , -3.424299  , -5.78160477, -2.99166799, -6.40561104,
        -3.85693002, -5.77898155, -2.99386433],
       [-5.84053135, -3.58799148, -5.5755229 , -3.12508106, -6.1055398 ,
        -4.05090189, -5.55508795, -3.13883638],
       [-5.5712471 , -3.72334242, -5.358634  , -3.23414803, -5.78386021,
        -4.21253681, -5.31733281, -3.2650041 ],
       [-5.28857565, -3.82788241, -5.13180017, -3.31804204, -5.44535112,
        -4.33772278, -5.06896284, -3.37528224],
       [-4.99599719, -3.9002316 , -4.89634323, -3.37622309, -5.09565115,
        -4.42424011, -4.81188653, -3.47150411],
       [-4.69726992, -3.94033349, -4.65293789, -3.40877891, -4.74160194,
        -4.47188807, -4.54747025, -3.55507221],
       [-4.39598441, -3.95027089, -4.38776588, -3.41693401, -4.40420294,
        -4.48360777, -4.27680613, -3.62721603],
       [-4.09447312, -3.94962215, -4.09492302, -3.4162221 , -4.09402323,
        -4.48302221, -4.00083524, -3.68911834],
       [-3.79296052, -3.94976199, -3.79268599, -3.41636205, -3.79323506,
        -4.48316193, -3.72028778, -3.74173143],
       [-3.49144852, -3.9499321 , -3.49128103, -3.41653204, -3.49161601,
        -4.48333216, -3.43579558, -3.7859425 ],
       [-3.18993604, -3.94995117, -3.18996811, -3.41655111, -3.18990397,
        -4.48335123, -3.14792299, -3.82260807],
       [-2.88842344, -3.94989598, -2.88850188, -3.41649604, -2.888345  ,
        -4.48329592, -2.85718364, -3.8525743 ],
       [-2.58691156, -3.94986248, -2.58695006, -3.41646194, -2.58687305,
        -4.48326302, -2.56405024, -3.87668771],
       [-2.28539944, -3.94985199, -2.28539991, -3.41645193, -2.28539896,
        -4.48325205, -2.26895373, -3.89578361],
       [-1.98388749, -3.94986153, -1.98387098, -3.41646099, -1.983904  ,
        -4.48326206, -1.97228011, -3.91066841],
       [-1.68237495, -3.94987059, -1.68236196, -3.41647005, -1.68238795,
        -4.48327112, -1.67434365, -3.92203171],
       [-1.38086301, -3.94987595, -1.38085699, -3.41647601, -1.38086903,
        -4.48327589, -1.37540941, -3.93048916],
       [-1.07935095, -3.94987738, -1.07935095, -3.41647696, -1.07935095,
        -4.4832778 , -1.07570351, -3.9366005 ],
       [-0.77783856, -3.94987595, -0.77784163, -3.41647601, -0.77783549,
        -4.48327589, -0.77542323, -3.94089182],
       [-0.47632641, -3.94987404, -0.476329  , -3.4164741 , -0.47632381,
        -4.48327398, -0.47472568, -3.94380986],
       [-0.1748142 , -3.94987297, -0.1748157 , -3.41647291, -0.1748127 ,
        -4.48327303, -0.17374315, -3.94575891],
       [ 0.126698  , -3.94987249,  0.1266976 , -3.41647196,  0.1266984 ,
        -4.48327303,  0.12741687, -3.94708641],
       [ 0.42821015, -3.94987249,  0.4282105 , -3.41647196,  0.42820981,
        -4.48327303,  0.42866174, -3.94810874],
       [ 0.72972235, -3.94987297,  0.72972292, -3.41647291,  0.72972178,
        -4.48327303,  0.72996587, -3.9489136 ],
       [ 1.0312345 , -3.94987297,  1.03123498, -3.41647291,  1.03123403,
        -4.48327303,  1.03133512, -3.94947388],
       [ 1.33274698, -3.94987297,  1.33274698, -3.41647291,  1.33274698,
        -4.48327303,  1.33276683, -3.94979337],
       [ 1.63425899, -3.94987297,  1.63425899, -3.41647291,  1.63425899,
        -4.48327303,  1.63425899, -3.94987297],
       [ 1.80577099, -3.94987297,  1.80577099, -3.41647291,  1.80577099,
        -4.48327303,  1.80577099, -3.94987297]]
import numpy as np

def dist(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def get_waypoints_ordered_in_driving_direction(params, waypoints):
    # waypoints are always provided in counter clock wise order
    if params['is_reversed']: # driving clock wise.
        return list(reversed(waypoints))
    else: # driving counter clock wise.
        return waypoints
    


def reward_function(params):
    '''
    Example of being near the nearest racing line 
    '''

    
    waypoints_input = np.array(get_racing_line_waypoints())
    racing_line = waypoints_input[:,6:8]
    waypoints = params["waypoints"]
    ordered_racing_line = get_waypoints_ordered_in_driving_direction(params, racing_line)
    ordered_waypoints = get_waypoints_ordered_in_driving_direction(params, waypoints)
    car = [params['x'], params['y']]
    distances = [dist(p, car) for p in ordered_waypoints]
    min_dist = min(distances)
    i_closest = distances.index(min_dist)
    #find the distance to the racing line point for the closest waypoint you are at
    dist_from_racingline = dist(car, ordered_racing_line[i_closest])
    #check for divide by 0 and then limit the reward to between 1 and 0.001 normally
    if dist_from_racingline == 0:
        #if it is exactly on the racing line give it an extra point
        reward = 2
    else:
        reward = 1/dist_from_racingline
        if reward > 10: reward =10
        if reward < 0.01: reward = 0.01
        reward = reward /10

    #add extra speed boost if in good track position
    
    if reward > 0.5:
        if params['speed']>3.0:
            reward = reward + 1
        if params['speed']>3.3:
            reward=reward+1
        if params['speed']>3.5:
            reward=reward+1
        if params['speed']>3.7:
            reward=reward+1
    return reward
    