{"filter":false,"title":"tests.py","tooltip":"/physical/tests.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":150,"column":0},"end":{"row":152,"column":37},"action":"remove","lines":["    ","        #self.bmr = self.bmr_calc()","        #self.TDEE = self.TDEE_calc()"],"id":510}],[{"start":{"row":150,"column":0},"end":{"row":151,"column":0},"action":"insert","lines":["",""],"id":511},{"start":{"row":151,"column":0},"end":{"row":152,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":149,"column":4},"end":{"row":150,"column":0},"action":"insert","lines":["",""],"id":512},{"start":{"row":150,"column":0},"end":{"row":150,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":150,"column":4},"end":{"row":156,"column":48},"action":"insert","lines":["    # Calculate user TDEE:","    def test_calculate_TDEE(self):","        \"\"\"TDEE calculated correctly\"\"\"","        metric = Macro.objects.get(unit_type=\"Metric\")","        imperial = Macro.objects.get(unit_type=\"Imperial\")","        self.assertEqual(metric.TDEE_calc(), 1836.48)","        self.assertEqual(imperial.TDEE_calc(), )"],"id":513}],[{"start":{"row":150,"column":4},"end":{"row":150,"column":8},"action":"remove","lines":["    "],"id":514}],[{"start":{"row":150,"column":21},"end":{"row":150,"column":25},"action":"remove","lines":["TDEE"],"id":515},{"start":{"row":150,"column":21},"end":{"row":150,"column":22},"action":"insert","lines":["D"]},{"start":{"row":150,"column":22},"end":{"row":150,"column":23},"action":"insert","lines":["A"]},{"start":{"row":150,"column":23},"end":{"row":150,"column":24},"action":"insert","lines":["I"]},{"start":{"row":150,"column":24},"end":{"row":150,"column":25},"action":"insert","lines":["L"]},{"start":{"row":150,"column":25},"end":{"row":150,"column":26},"action":"insert","lines":["Y"]}],[{"start":{"row":150,"column":26},"end":{"row":150,"column":27},"action":"insert","lines":[" "],"id":516},{"start":{"row":150,"column":27},"end":{"row":150,"column":28},"action":"insert","lines":["C"]},{"start":{"row":150,"column":28},"end":{"row":150,"column":29},"action":"insert","lines":["A"]},{"start":{"row":150,"column":29},"end":{"row":150,"column":30},"action":"insert","lines":["L"]},{"start":{"row":150,"column":30},"end":{"row":150,"column":31},"action":"insert","lines":["O"]},{"start":{"row":150,"column":31},"end":{"row":150,"column":32},"action":"insert","lines":["R"]},{"start":{"row":150,"column":32},"end":{"row":150,"column":33},"action":"insert","lines":["I"]},{"start":{"row":150,"column":33},"end":{"row":150,"column":34},"action":"insert","lines":["E"]}],[{"start":{"row":150,"column":33},"end":{"row":150,"column":34},"action":"remove","lines":["E"],"id":517},{"start":{"row":150,"column":32},"end":{"row":150,"column":33},"action":"remove","lines":["I"]},{"start":{"row":150,"column":31},"end":{"row":150,"column":32},"action":"remove","lines":["R"]},{"start":{"row":150,"column":30},"end":{"row":150,"column":31},"action":"remove","lines":["O"]},{"start":{"row":150,"column":29},"end":{"row":150,"column":30},"action":"remove","lines":["L"]},{"start":{"row":150,"column":28},"end":{"row":150,"column":29},"action":"remove","lines":["A"]},{"start":{"row":150,"column":27},"end":{"row":150,"column":28},"action":"remove","lines":["C"]},{"start":{"row":150,"column":26},"end":{"row":150,"column":27},"action":"remove","lines":[" "]},{"start":{"row":150,"column":25},"end":{"row":150,"column":26},"action":"remove","lines":["Y"]},{"start":{"row":150,"column":24},"end":{"row":150,"column":25},"action":"remove","lines":["L"]},{"start":{"row":150,"column":23},"end":{"row":150,"column":24},"action":"remove","lines":["I"]},{"start":{"row":150,"column":22},"end":{"row":150,"column":23},"action":"remove","lines":["A"]},{"start":{"row":150,"column":21},"end":{"row":150,"column":22},"action":"remove","lines":["D"]}],[{"start":{"row":150,"column":21},"end":{"row":150,"column":22},"action":"insert","lines":["d"],"id":518},{"start":{"row":150,"column":22},"end":{"row":150,"column":23},"action":"insert","lines":["a"]},{"start":{"row":150,"column":23},"end":{"row":150,"column":24},"action":"insert","lines":["i"]},{"start":{"row":150,"column":24},"end":{"row":150,"column":25},"action":"insert","lines":["l"]},{"start":{"row":150,"column":25},"end":{"row":150,"column":26},"action":"insert","lines":["y"]}],[{"start":{"row":150,"column":26},"end":{"row":150,"column":27},"action":"insert","lines":[" "],"id":519},{"start":{"row":150,"column":27},"end":{"row":150,"column":28},"action":"insert","lines":["c"]},{"start":{"row":150,"column":28},"end":{"row":150,"column":29},"action":"insert","lines":["a"]},{"start":{"row":150,"column":29},"end":{"row":150,"column":30},"action":"insert","lines":["l"]},{"start":{"row":150,"column":30},"end":{"row":150,"column":31},"action":"insert","lines":["o"]},{"start":{"row":150,"column":31},"end":{"row":150,"column":32},"action":"insert","lines":["r"]},{"start":{"row":150,"column":32},"end":{"row":150,"column":33},"action":"insert","lines":["i"]},{"start":{"row":150,"column":33},"end":{"row":150,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":150,"column":34},"end":{"row":150,"column":35},"action":"insert","lines":[" "],"id":520},{"start":{"row":150,"column":35},"end":{"row":150,"column":36},"action":"insert","lines":["g"]},{"start":{"row":150,"column":36},"end":{"row":150,"column":37},"action":"insert","lines":["o"]},{"start":{"row":150,"column":37},"end":{"row":150,"column":38},"action":"insert","lines":["a"]},{"start":{"row":150,"column":38},"end":{"row":150,"column":39},"action":"insert","lines":["l"]}],[{"start":{"row":151,"column":23},"end":{"row":151,"column":27},"action":"remove","lines":["TDEE"],"id":521},{"start":{"row":151,"column":23},"end":{"row":151,"column":24},"action":"insert","lines":["d"]},{"start":{"row":151,"column":24},"end":{"row":151,"column":25},"action":"insert","lines":["a"]},{"start":{"row":151,"column":25},"end":{"row":151,"column":26},"action":"insert","lines":["i"]},{"start":{"row":151,"column":26},"end":{"row":151,"column":27},"action":"insert","lines":["l"]},{"start":{"row":151,"column":27},"end":{"row":151,"column":28},"action":"insert","lines":["y"]},{"start":{"row":151,"column":28},"end":{"row":151,"column":29},"action":"insert","lines":["_"]},{"start":{"row":151,"column":29},"end":{"row":151,"column":30},"action":"insert","lines":["c"]},{"start":{"row":151,"column":30},"end":{"row":151,"column":31},"action":"insert","lines":["a"]},{"start":{"row":151,"column":31},"end":{"row":151,"column":32},"action":"insert","lines":["l"]},{"start":{"row":151,"column":32},"end":{"row":151,"column":33},"action":"insert","lines":["o"]}],[{"start":{"row":151,"column":33},"end":{"row":151,"column":34},"action":"insert","lines":["r"],"id":522},{"start":{"row":151,"column":34},"end":{"row":151,"column":35},"action":"insert","lines":["i"]},{"start":{"row":151,"column":35},"end":{"row":151,"column":36},"action":"insert","lines":["e"]},{"start":{"row":151,"column":36},"end":{"row":151,"column":37},"action":"insert","lines":["_"]},{"start":{"row":151,"column":37},"end":{"row":151,"column":38},"action":"insert","lines":["g"]},{"start":{"row":151,"column":38},"end":{"row":151,"column":39},"action":"insert","lines":["o"]},{"start":{"row":151,"column":39},"end":{"row":151,"column":40},"action":"insert","lines":["a"]},{"start":{"row":151,"column":40},"end":{"row":151,"column":41},"action":"insert","lines":["l"]}],[{"start":{"row":152,"column":11},"end":{"row":152,"column":15},"action":"remove","lines":["TDEE"],"id":523},{"start":{"row":152,"column":11},"end":{"row":152,"column":12},"action":"insert","lines":["C"]},{"start":{"row":152,"column":12},"end":{"row":152,"column":13},"action":"insert","lines":["a"]},{"start":{"row":152,"column":13},"end":{"row":152,"column":14},"action":"insert","lines":["l"]},{"start":{"row":152,"column":14},"end":{"row":152,"column":15},"action":"insert","lines":["o"]},{"start":{"row":152,"column":15},"end":{"row":152,"column":16},"action":"insert","lines":["r"]},{"start":{"row":152,"column":16},"end":{"row":152,"column":17},"action":"insert","lines":["i"]},{"start":{"row":152,"column":17},"end":{"row":152,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":152,"column":18},"end":{"row":152,"column":19},"action":"insert","lines":[" "],"id":524},{"start":{"row":152,"column":19},"end":{"row":152,"column":20},"action":"insert","lines":["g"]},{"start":{"row":152,"column":20},"end":{"row":152,"column":21},"action":"insert","lines":["o"]},{"start":{"row":152,"column":21},"end":{"row":152,"column":22},"action":"insert","lines":["a"]},{"start":{"row":152,"column":22},"end":{"row":152,"column":23},"action":"insert","lines":["l"]}],[{"start":{"row":155,"column":32},"end":{"row":155,"column":41},"action":"remove","lines":["TDEE_calc"],"id":525},{"start":{"row":155,"column":32},"end":{"row":155,"column":55},"action":"insert","lines":["calculated_calorie_goal"]}],[{"start":{"row":156,"column":34},"end":{"row":156,"column":43},"action":"remove","lines":["TDEE_calc"],"id":526},{"start":{"row":156,"column":34},"end":{"row":156,"column":57},"action":"insert","lines":["calculated_calorie_goal"]}],[{"start":{"row":155,"column":59},"end":{"row":155,"column":63},"action":"remove","lines":["1836"],"id":527}],[{"start":{"row":155,"column":61},"end":{"row":155,"column":62},"action":"remove","lines":["8"],"id":528},{"start":{"row":155,"column":60},"end":{"row":155,"column":61},"action":"remove","lines":["4"]},{"start":{"row":155,"column":59},"end":{"row":155,"column":60},"action":"remove","lines":["."]}],[{"start":{"row":155,"column":59},"end":{"row":155,"column":66},"action":"insert","lines":["1561.01"],"id":529}],[{"start":{"row":158,"column":0},"end":{"row":160,"column":65},"action":"remove","lines":["","","        #self.daily_calorie_goal = self.calculated_calorie_goal()"],"id":530}],[{"start":{"row":157,"column":0},"end":{"row":157,"column":4},"action":"insert","lines":["    "],"id":531}],[{"start":{"row":157,"column":4},"end":{"row":158,"column":0},"action":"insert","lines":["",""],"id":532},{"start":{"row":158,"column":0},"end":{"row":158,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":158,"column":4},"end":{"row":164,"column":62},"action":"insert","lines":["    # Calculate user daily calorie goal:","    def test_calculate_daily_calorie_goal(self):","        \"\"\"Calorie goal calculated correctly\"\"\"","        metric = Macro.objects.get(unit_type=\"Metric\")","        imperial = Macro.objects.get(unit_type=\"Imperial\")","        self.assertEqual(metric.calculated_calorie_goal(), 1561.01)","        self.assertEqual(imperial.calculated_calorie_goal(), )"],"id":533}],[{"start":{"row":158,"column":4},"end":{"row":158,"column":8},"action":"remove","lines":["    "],"id":534}],[{"start":{"row":158,"column":29},"end":{"row":158,"column":39},"action":"remove","lines":["lorie goal"],"id":535},{"start":{"row":158,"column":29},"end":{"row":158,"column":30},"action":"insert","lines":["r"]},{"start":{"row":158,"column":30},"end":{"row":158,"column":31},"action":"insert","lines":["b"]}],[{"start":{"row":158,"column":31},"end":{"row":158,"column":32},"action":"insert","lines":[" "],"id":536},{"start":{"row":158,"column":32},"end":{"row":158,"column":33},"action":"insert","lines":["w"]},{"start":{"row":158,"column":33},"end":{"row":158,"column":34},"action":"insert","lines":["e"]},{"start":{"row":158,"column":34},"end":{"row":158,"column":35},"action":"insert","lines":["i"]},{"start":{"row":158,"column":35},"end":{"row":158,"column":36},"action":"insert","lines":["g"]},{"start":{"row":158,"column":36},"end":{"row":158,"column":37},"action":"insert","lines":["h"]},{"start":{"row":158,"column":37},"end":{"row":158,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":159,"column":31},"end":{"row":159,"column":41},"action":"remove","lines":["lorie_goal"],"id":537},{"start":{"row":159,"column":31},"end":{"row":159,"column":32},"action":"insert","lines":["r"]},{"start":{"row":159,"column":32},"end":{"row":159,"column":33},"action":"insert","lines":["b"]},{"start":{"row":159,"column":33},"end":{"row":159,"column":34},"action":"insert","lines":["_"]},{"start":{"row":159,"column":34},"end":{"row":159,"column":35},"action":"insert","lines":["w"]},{"start":{"row":159,"column":35},"end":{"row":159,"column":36},"action":"insert","lines":["e"]},{"start":{"row":159,"column":36},"end":{"row":159,"column":37},"action":"insert","lines":["i"]},{"start":{"row":159,"column":37},"end":{"row":159,"column":38},"action":"insert","lines":["g"]},{"start":{"row":159,"column":38},"end":{"row":159,"column":39},"action":"insert","lines":["h"]},{"start":{"row":159,"column":39},"end":{"row":159,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":160,"column":13},"end":{"row":160,"column":23},"action":"remove","lines":["lorie goal"],"id":538},{"start":{"row":160,"column":13},"end":{"row":160,"column":14},"action":"insert","lines":["r"]},{"start":{"row":160,"column":14},"end":{"row":160,"column":15},"action":"insert","lines":["b"]}],[{"start":{"row":160,"column":15},"end":{"row":160,"column":16},"action":"insert","lines":[" "],"id":539},{"start":{"row":160,"column":16},"end":{"row":160,"column":17},"action":"insert","lines":["w"]},{"start":{"row":160,"column":17},"end":{"row":160,"column":18},"action":"insert","lines":["e"]},{"start":{"row":160,"column":18},"end":{"row":160,"column":19},"action":"insert","lines":["i"]},{"start":{"row":160,"column":19},"end":{"row":160,"column":20},"action":"insert","lines":["g"]},{"start":{"row":160,"column":20},"end":{"row":160,"column":21},"action":"insert","lines":["h"]},{"start":{"row":160,"column":21},"end":{"row":160,"column":22},"action":"insert","lines":["t"]}],[{"start":{"row":163,"column":32},"end":{"row":163,"column":55},"action":"remove","lines":["calculated_calorie_goal"],"id":540},{"start":{"row":163,"column":32},"end":{"row":163,"column":41},"action":"insert","lines":["carb_calc"]}],[{"start":{"row":164,"column":34},"end":{"row":164,"column":57},"action":"remove","lines":["calculated_calorie_goal"],"id":541},{"start":{"row":164,"column":34},"end":{"row":164,"column":43},"action":"insert","lines":["carb_calc"]}],[{"start":{"row":163,"column":45},"end":{"row":163,"column":52},"action":"remove","lines":["1561.01"],"id":542},{"start":{"row":163,"column":45},"end":{"row":163,"column":46},"action":"insert","lines":["1"]},{"start":{"row":163,"column":46},"end":{"row":163,"column":47},"action":"insert","lines":["1"]},{"start":{"row":163,"column":47},"end":{"row":163,"column":48},"action":"insert","lines":["7"]},{"start":{"row":163,"column":48},"end":{"row":163,"column":49},"action":"insert","lines":["."]},{"start":{"row":163,"column":49},"end":{"row":163,"column":50},"action":"insert","lines":["0"]},{"start":{"row":163,"column":50},"end":{"row":163,"column":51},"action":"insert","lines":["0"]}],[{"start":{"row":164,"column":48},"end":{"row":166,"column":44},"action":"remove","lines":["","","        #self.carb_weight = self.carb_calc()"],"id":543}],[{"start":{"row":164,"column":48},"end":{"row":165,"column":0},"action":"insert","lines":["",""],"id":544},{"start":{"row":165,"column":0},"end":{"row":165,"column":8},"action":"insert","lines":["        "]},{"start":{"row":165,"column":8},"end":{"row":166,"column":0},"action":"insert","lines":["",""]},{"start":{"row":166,"column":0},"end":{"row":166,"column":8},"action":"insert","lines":["        "]},{"start":{"row":166,"column":8},"end":{"row":167,"column":0},"action":"insert","lines":["",""]},{"start":{"row":167,"column":0},"end":{"row":167,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":165,"column":0},"end":{"row":166,"column":0},"action":"insert","lines":["",""],"id":545}],[{"start":{"row":166,"column":0},"end":{"row":172,"column":48},"action":"insert","lines":["    # Calculate user daily carb weight:","    def test_calculate_daily_carb_weight(self):","        \"\"\"Carb weight calculated correctly\"\"\"","        metric = Macro.objects.get(unit_type=\"Metric\")","        imperial = Macro.objects.get(unit_type=\"Imperial\")","        self.assertEqual(metric.carb_calc(), 117.00)","        self.assertEqual(imperial.carb_calc(), )"],"id":546}],[{"start":{"row":166,"column":27},"end":{"row":166,"column":32},"action":"remove","lines":["carb "],"id":547},{"start":{"row":166,"column":27},"end":{"row":166,"column":28},"action":"insert","lines":["p"]},{"start":{"row":166,"column":28},"end":{"row":166,"column":29},"action":"insert","lines":["r"]},{"start":{"row":166,"column":29},"end":{"row":166,"column":30},"action":"insert","lines":["o"]},{"start":{"row":166,"column":30},"end":{"row":166,"column":31},"action":"insert","lines":["t"]},{"start":{"row":166,"column":31},"end":{"row":166,"column":32},"action":"insert","lines":["e"]},{"start":{"row":166,"column":32},"end":{"row":166,"column":33},"action":"insert","lines":["i"]},{"start":{"row":166,"column":33},"end":{"row":166,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":166,"column":34},"end":{"row":166,"column":35},"action":"insert","lines":[" "],"id":548}],[{"start":{"row":167,"column":29},"end":{"row":167,"column":33},"action":"remove","lines":["carb"],"id":549},{"start":{"row":167,"column":29},"end":{"row":167,"column":30},"action":"insert","lines":["p"]},{"start":{"row":167,"column":30},"end":{"row":167,"column":31},"action":"insert","lines":["r"]},{"start":{"row":167,"column":31},"end":{"row":167,"column":32},"action":"insert","lines":["o"]},{"start":{"row":167,"column":32},"end":{"row":167,"column":33},"action":"insert","lines":["t"]},{"start":{"row":167,"column":33},"end":{"row":167,"column":34},"action":"insert","lines":["e"]},{"start":{"row":167,"column":34},"end":{"row":167,"column":35},"action":"insert","lines":["i"]},{"start":{"row":167,"column":35},"end":{"row":167,"column":36},"action":"insert","lines":["n"]}],[{"start":{"row":168,"column":11},"end":{"row":168,"column":15},"action":"remove","lines":["Carb"],"id":550},{"start":{"row":168,"column":11},"end":{"row":168,"column":12},"action":"insert","lines":["P"]},{"start":{"row":168,"column":12},"end":{"row":168,"column":13},"action":"insert","lines":["r"]},{"start":{"row":168,"column":13},"end":{"row":168,"column":14},"action":"insert","lines":["o"]},{"start":{"row":168,"column":14},"end":{"row":168,"column":15},"action":"insert","lines":["e"]},{"start":{"row":168,"column":15},"end":{"row":168,"column":16},"action":"insert","lines":["t"]},{"start":{"row":168,"column":16},"end":{"row":168,"column":17},"action":"insert","lines":["i"]},{"start":{"row":168,"column":17},"end":{"row":168,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":168,"column":17},"end":{"row":168,"column":18},"action":"remove","lines":["n"],"id":551},{"start":{"row":168,"column":16},"end":{"row":168,"column":17},"action":"remove","lines":["i"]},{"start":{"row":168,"column":15},"end":{"row":168,"column":16},"action":"remove","lines":["t"]},{"start":{"row":168,"column":14},"end":{"row":168,"column":15},"action":"remove","lines":["e"]}],[{"start":{"row":168,"column":14},"end":{"row":168,"column":15},"action":"insert","lines":["t"],"id":552},{"start":{"row":168,"column":15},"end":{"row":168,"column":16},"action":"insert","lines":["e"]},{"start":{"row":168,"column":16},"end":{"row":168,"column":17},"action":"insert","lines":["i"]},{"start":{"row":168,"column":17},"end":{"row":168,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":171,"column":32},"end":{"row":171,"column":36},"action":"remove","lines":["carb"],"id":553},{"start":{"row":171,"column":32},"end":{"row":171,"column":33},"action":"insert","lines":["p"]},{"start":{"row":171,"column":33},"end":{"row":171,"column":34},"action":"insert","lines":["r"]},{"start":{"row":171,"column":34},"end":{"row":171,"column":35},"action":"insert","lines":["o"]},{"start":{"row":171,"column":35},"end":{"row":171,"column":36},"action":"insert","lines":["t"]},{"start":{"row":171,"column":36},"end":{"row":171,"column":37},"action":"insert","lines":["e"]},{"start":{"row":171,"column":37},"end":{"row":171,"column":38},"action":"insert","lines":["i"]},{"start":{"row":171,"column":38},"end":{"row":171,"column":39},"action":"insert","lines":["n"]}],[{"start":{"row":172,"column":34},"end":{"row":172,"column":38},"action":"remove","lines":["carb"],"id":554},{"start":{"row":172,"column":34},"end":{"row":172,"column":35},"action":"insert","lines":["p"]},{"start":{"row":172,"column":35},"end":{"row":172,"column":36},"action":"insert","lines":["r"]},{"start":{"row":172,"column":36},"end":{"row":172,"column":37},"action":"insert","lines":["o"]},{"start":{"row":172,"column":37},"end":{"row":172,"column":38},"action":"insert","lines":["t"]},{"start":{"row":172,"column":38},"end":{"row":172,"column":39},"action":"insert","lines":["e"]},{"start":{"row":172,"column":39},"end":{"row":172,"column":40},"action":"insert","lines":["i"]},{"start":{"row":172,"column":40},"end":{"row":172,"column":41},"action":"insert","lines":["n"]}],[{"start":{"row":171,"column":49},"end":{"row":171,"column":51},"action":"remove","lines":["17"],"id":555},{"start":{"row":171,"column":49},"end":{"row":171,"column":50},"action":"insert","lines":["5"]},{"start":{"row":171,"column":50},"end":{"row":171,"column":51},"action":"insert","lines":["6"]}],[{"start":{"row":173,"column":0},"end":{"row":174,"column":0},"action":"insert","lines":["",""],"id":556}],[{"start":{"row":174,"column":0},"end":{"row":180,"column":53},"action":"insert","lines":["    # Calculate user daily protein weight:","    def test_calculate_daily_protein_weight(self):","        \"\"\"Protein weight calculated correctly\"\"\"","        metric = Macro.objects.get(unit_type=\"Metric\")","        imperial = Macro.objects.get(unit_type=\"Imperial\")","        self.assertEqual(metric.protein_calc(), 156.00)","        self.assertEqual(imperial.protein_calc(), )  "],"id":557}],[{"start":{"row":180,"column":53},"end":{"row":180,"column":61},"action":"remove","lines":["        "],"id":558},{"start":{"row":180,"column":53},"end":{"row":181,"column":0},"action":"insert","lines":["",""]},{"start":{"row":181,"column":0},"end":{"row":181,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":174,"column":27},"end":{"row":174,"column":34},"action":"remove","lines":["protein"],"id":559},{"start":{"row":174,"column":27},"end":{"row":174,"column":28},"action":"insert","lines":["f"]},{"start":{"row":174,"column":28},"end":{"row":174,"column":29},"action":"insert","lines":["a"]},{"start":{"row":174,"column":29},"end":{"row":174,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":175,"column":29},"end":{"row":175,"column":36},"action":"remove","lines":["protein"],"id":560},{"start":{"row":175,"column":29},"end":{"row":175,"column":30},"action":"insert","lines":["f"]},{"start":{"row":175,"column":30},"end":{"row":175,"column":31},"action":"insert","lines":["a"]},{"start":{"row":175,"column":31},"end":{"row":175,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":176,"column":11},"end":{"row":176,"column":18},"action":"remove","lines":["Protein"],"id":561},{"start":{"row":176,"column":11},"end":{"row":176,"column":12},"action":"insert","lines":["F"]},{"start":{"row":176,"column":12},"end":{"row":176,"column":13},"action":"insert","lines":["a"]},{"start":{"row":176,"column":13},"end":{"row":176,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":179,"column":32},"end":{"row":179,"column":39},"action":"remove","lines":["protein"],"id":562},{"start":{"row":179,"column":32},"end":{"row":179,"column":33},"action":"insert","lines":["f"]},{"start":{"row":179,"column":33},"end":{"row":179,"column":34},"action":"insert","lines":["a"]},{"start":{"row":179,"column":34},"end":{"row":179,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":180,"column":34},"end":{"row":180,"column":41},"action":"remove","lines":["protein"],"id":563},{"start":{"row":180,"column":34},"end":{"row":180,"column":35},"action":"insert","lines":["f"]},{"start":{"row":180,"column":35},"end":{"row":180,"column":36},"action":"insert","lines":["a"]},{"start":{"row":180,"column":36},"end":{"row":180,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":179,"column":46},"end":{"row":179,"column":47},"action":"remove","lines":["6"],"id":564}],[{"start":{"row":179,"column":46},"end":{"row":179,"column":47},"action":"insert","lines":["2"],"id":565}],[{"start":{"row":179,"column":44},"end":{"row":179,"column":45},"action":"remove","lines":["1"],"id":566}],[{"start":{"row":187,"column":51},"end":{"row":189,"column":55},"action":"remove","lines":["","        #self.unit_height= self.calculate_unit_height()","        #self.unit_weight= self.calculate_unit_weight()"],"id":567}],[{"start":{"row":182,"column":0},"end":{"row":184,"column":42},"action":"remove","lines":["        ","        #self.protein_weight = self.protein_calc()","        #self.fat_weight = self.fat_calc()"],"id":568}],[{"start":{"row":181,"column":1},"end":{"row":181,"column":2},"action":"remove","lines":[" "],"id":569},{"start":{"row":181,"column":0},"end":{"row":181,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":180,"column":49},"end":{"row":181,"column":6},"action":"remove","lines":["","      "],"id":570}],[{"start":{"row":180,"column":49},"end":{"row":181,"column":0},"action":"insert","lines":["",""],"id":571},{"start":{"row":181,"column":0},"end":{"row":181,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":181,"column":4},"end":{"row":181,"column":8},"action":"remove","lines":["    "],"id":572},{"start":{"row":181,"column":0},"end":{"row":181,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":181,"column":0},"end":{"row":182,"column":0},"action":"insert","lines":["",""],"id":573}],[{"start":{"row":182,"column":0},"end":{"row":204,"column":49},"action":"insert","lines":["    # Calculate user daily carb weight:","    def test_calculate_daily_carb_weight(self):","        \"\"\"Carb weight calculated correctly\"\"\"","        metric = Macro.objects.get(unit_type=\"Metric\")","        imperial = Macro.objects.get(unit_type=\"Imperial\")","        self.assertEqual(metric.carb_calc(), 117.00)","        self.assertEqual(imperial.carb_calc(), )","","    # Calculate user daily protein weight:","    def test_calculate_daily_protein_weight(self):","        \"\"\"Protein weight calculated correctly\"\"\"","        metric = Macro.objects.get(unit_type=\"Metric\")","        imperial = Macro.objects.get(unit_type=\"Imperial\")","        self.assertEqual(metric.protein_calc(), 156.00)","        self.assertEqual(imperial.protein_calc(), )        ","","    # Calculate user daily fat weight:","    def test_calculate_daily_fat_weight(self):","        \"\"\"Fat weight calculated correctly\"\"\"","        metric = Macro.objects.get(unit_type=\"Metric\")","        imperial = Macro.objects.get(unit_type=\"Imperial\")","        self.assertEqual(metric.fat_calc(), 52.00)","        self.assertEqual(imperial.fat_calc(), )  "],"id":574}],[{"start":{"row":182,"column":32},"end":{"row":182,"column":38},"action":"remove","lines":["weight"],"id":575},{"start":{"row":182,"column":32},"end":{"row":182,"column":33},"action":"insert","lines":["p"]},{"start":{"row":182,"column":33},"end":{"row":182,"column":34},"action":"insert","lines":["e"]},{"start":{"row":182,"column":34},"end":{"row":182,"column":35},"action":"insert","lines":["r"]},{"start":{"row":182,"column":35},"end":{"row":182,"column":36},"action":"insert","lines":["c"]},{"start":{"row":182,"column":36},"end":{"row":182,"column":37},"action":"insert","lines":["e"]},{"start":{"row":182,"column":37},"end":{"row":182,"column":38},"action":"insert","lines":["n"]},{"start":{"row":182,"column":38},"end":{"row":182,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":184,"column":16},"end":{"row":184,"column":22},"action":"remove","lines":["weight"],"id":576},{"start":{"row":184,"column":16},"end":{"row":184,"column":23},"action":"insert","lines":["percent"]}],[{"start":{"row":183,"column":34},"end":{"row":183,"column":40},"action":"remove","lines":["weight"],"id":577},{"start":{"row":183,"column":34},"end":{"row":183,"column":41},"action":"insert","lines":["percent"]}],[{"start":{"row":187,"column":36},"end":{"row":187,"column":37},"action":"insert","lines":["_"],"id":578}],[{"start":{"row":187,"column":37},"end":{"row":187,"column":44},"action":"insert","lines":["percent"],"id":579}],[{"start":{"row":188,"column":38},"end":{"row":188,"column":39},"action":"insert","lines":["_"],"id":580}],[{"start":{"row":188,"column":39},"end":{"row":188,"column":46},"action":"insert","lines":["percent"],"id":581}],[{"start":{"row":187,"column":53},"end":{"row":187,"column":56},"action":"remove","lines":["117"],"id":582},{"start":{"row":187,"column":53},"end":{"row":187,"column":54},"action":"insert","lines":["3"]},{"start":{"row":187,"column":54},"end":{"row":187,"column":55},"action":"insert","lines":["0"]}],[{"start":{"row":191,"column":37},"end":{"row":191,"column":43},"action":"remove","lines":["weight"],"id":583},{"start":{"row":191,"column":37},"end":{"row":191,"column":44},"action":"insert","lines":["percent"]}],[{"start":{"row":192,"column":19},"end":{"row":192,"column":25},"action":"remove","lines":["weight"],"id":584},{"start":{"row":192,"column":19},"end":{"row":192,"column":26},"action":"insert","lines":["percent"]}],[{"start":{"row":195,"column":39},"end":{"row":195,"column":40},"action":"insert","lines":["_"],"id":585}],[{"start":{"row":195,"column":40},"end":{"row":195,"column":47},"action":"insert","lines":["percent"],"id":586}],[{"start":{"row":196,"column":41},"end":{"row":196,"column":42},"action":"insert","lines":["_"],"id":587}],[{"start":{"row":196,"column":42},"end":{"row":196,"column":49},"action":"insert","lines":["percent"],"id":588}],[{"start":{"row":195,"column":56},"end":{"row":195,"column":59},"action":"remove","lines":["156"],"id":589},{"start":{"row":195,"column":56},"end":{"row":195,"column":57},"action":"insert","lines":["4"]},{"start":{"row":195,"column":57},"end":{"row":195,"column":58},"action":"insert","lines":["0"]}],[{"start":{"row":198,"column":31},"end":{"row":198,"column":37},"action":"remove","lines":["weight"],"id":590},{"start":{"row":198,"column":31},"end":{"row":198,"column":38},"action":"insert","lines":["percent"]}],[{"start":{"row":199,"column":33},"end":{"row":199,"column":39},"action":"remove","lines":["weight"],"id":591},{"start":{"row":199,"column":33},"end":{"row":199,"column":40},"action":"insert","lines":["percent"]}],[{"start":{"row":203,"column":35},"end":{"row":203,"column":36},"action":"insert","lines":["_"],"id":592}],[{"start":{"row":203,"column":36},"end":{"row":203,"column":43},"action":"insert","lines":["percent"],"id":593}],[{"start":{"row":204,"column":37},"end":{"row":204,"column":38},"action":"insert","lines":["_"],"id":594}],[{"start":{"row":204,"column":38},"end":{"row":204,"column":45},"action":"insert","lines":["percent"],"id":595}],[{"start":{"row":203,"column":52},"end":{"row":203,"column":54},"action":"remove","lines":["52"],"id":596},{"start":{"row":203,"column":52},"end":{"row":203,"column":53},"action":"insert","lines":["3"]},{"start":{"row":203,"column":53},"end":{"row":203,"column":54},"action":"insert","lines":["0"]}],[{"start":{"row":205,"column":0},"end":{"row":209,"column":0},"action":"remove","lines":["","        #self.carb_percent = self.carb_percent_calc()","        #self.protein_percent = self.protein_percent_calc()","        #self.fat_percent = self.fat_percent_calc()",""],"id":597}],[{"start":{"row":204,"column":57},"end":{"row":205,"column":0},"action":"remove","lines":["",""],"id":598}],[{"start":{"row":140,"column":46},"end":{"row":140,"column":53},"action":"insert","lines":["1791.05"],"id":599}],[{"start":{"row":148,"column":47},"end":{"row":148,"column":54},"action":"insert","lines":["3089.56"],"id":600}],[{"start":{"row":156,"column":61},"end":{"row":156,"column":68},"action":"insert","lines":["3089.56"],"id":601}],[{"start":{"row":188,"column":55},"end":{"row":188,"column":56},"action":"insert","lines":["4"],"id":602},{"start":{"row":188,"column":56},"end":{"row":188,"column":57},"action":"insert","lines":["0"]},{"start":{"row":188,"column":57},"end":{"row":188,"column":58},"action":"insert","lines":["."]},{"start":{"row":188,"column":58},"end":{"row":188,"column":59},"action":"insert","lines":["0"]},{"start":{"row":188,"column":59},"end":{"row":188,"column":60},"action":"insert","lines":["0"]}],[{"start":{"row":196,"column":58},"end":{"row":196,"column":59},"action":"insert","lines":["3"],"id":603},{"start":{"row":196,"column":59},"end":{"row":196,"column":60},"action":"insert","lines":["0"]},{"start":{"row":196,"column":60},"end":{"row":196,"column":61},"action":"insert","lines":["."]},{"start":{"row":196,"column":61},"end":{"row":196,"column":62},"action":"insert","lines":["0"]},{"start":{"row":196,"column":62},"end":{"row":196,"column":63},"action":"insert","lines":["0"]}],[{"start":{"row":204,"column":54},"end":{"row":204,"column":55},"action":"insert","lines":["3"],"id":604},{"start":{"row":204,"column":55},"end":{"row":204,"column":56},"action":"insert","lines":["0"]},{"start":{"row":204,"column":56},"end":{"row":204,"column":57},"action":"insert","lines":["."]},{"start":{"row":204,"column":57},"end":{"row":204,"column":58},"action":"insert","lines":["0"]},{"start":{"row":204,"column":58},"end":{"row":204,"column":59},"action":"insert","lines":["0"]}],[{"start":{"row":172,"column":50},"end":{"row":172,"column":51},"action":"insert","lines":["3"],"id":605},{"start":{"row":172,"column":51},"end":{"row":172,"column":52},"action":"insert","lines":["0"]},{"start":{"row":172,"column":52},"end":{"row":172,"column":53},"action":"insert","lines":["9"]},{"start":{"row":172,"column":53},"end":{"row":172,"column":54},"action":"insert","lines":["."]},{"start":{"row":172,"column":54},"end":{"row":172,"column":55},"action":"insert","lines":["0"]},{"start":{"row":172,"column":55},"end":{"row":172,"column":56},"action":"insert","lines":["0"]}],[{"start":{"row":164,"column":47},"end":{"row":164,"column":48},"action":"insert","lines":["3"],"id":606},{"start":{"row":164,"column":48},"end":{"row":164,"column":49},"action":"insert","lines":["0"]},{"start":{"row":164,"column":49},"end":{"row":164,"column":50},"action":"insert","lines":["9"]},{"start":{"row":164,"column":50},"end":{"row":164,"column":51},"action":"insert","lines":["."]},{"start":{"row":164,"column":51},"end":{"row":164,"column":52},"action":"insert","lines":["0"]},{"start":{"row":164,"column":52},"end":{"row":164,"column":53},"action":"insert","lines":["0"]}],[{"start":{"row":172,"column":50},"end":{"row":172,"column":56},"action":"remove","lines":["309.00"],"id":608},{"start":{"row":172,"column":50},"end":{"row":172,"column":51},"action":"insert","lines":["3"]}],[{"start":{"row":172,"column":50},"end":{"row":172,"column":51},"action":"remove","lines":["3"],"id":609}],[{"start":{"row":172,"column":50},"end":{"row":172,"column":51},"action":"insert","lines":["2"],"id":610},{"start":{"row":172,"column":51},"end":{"row":172,"column":52},"action":"insert","lines":["3"]},{"start":{"row":172,"column":52},"end":{"row":172,"column":53},"action":"insert","lines":["2"]},{"start":{"row":172,"column":53},"end":{"row":172,"column":54},"action":"insert","lines":["."]},{"start":{"row":172,"column":54},"end":{"row":172,"column":55},"action":"insert","lines":["0"]},{"start":{"row":172,"column":55},"end":{"row":172,"column":56},"action":"insert","lines":["0"]}],[{"start":{"row":180,"column":46},"end":{"row":180,"column":47},"action":"insert","lines":["1"],"id":611},{"start":{"row":180,"column":47},"end":{"row":180,"column":48},"action":"insert","lines":["0"]},{"start":{"row":180,"column":48},"end":{"row":180,"column":49},"action":"insert","lines":["3"]},{"start":{"row":180,"column":49},"end":{"row":180,"column":50},"action":"insert","lines":["."]},{"start":{"row":180,"column":50},"end":{"row":180,"column":51},"action":"insert","lines":["0"]},{"start":{"row":180,"column":51},"end":{"row":180,"column":52},"action":"insert","lines":["0"]}]]},"ace":{"folds":[],"scrolltop":2241,"scrollleft":0,"selection":{"start":{"row":186,"column":58},"end":{"row":186,"column":58},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":159,"state":"start","mode":"ace/mode/python"}},"timestamp":1597683234101,"hash":"5e6c906ae92a4b74ddf05b0597a660c756efd4ff"}