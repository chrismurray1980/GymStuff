{"filter":false,"title":"tests.py","tooltip":"/physical/tests.py","undoManager":{"mark":73,"position":73,"stack":[[{"start":{"row":99,"column":65},"end":{"row":99,"column":66},"action":"insert","lines":["."],"id":2},{"start":{"row":99,"column":66},"end":{"row":99,"column":67},"action":"insert","lines":["h"]},{"start":{"row":99,"column":67},"end":{"row":99,"column":68},"action":"insert","lines":["e"]},{"start":{"row":99,"column":68},"end":{"row":99,"column":69},"action":"insert","lines":["i"]},{"start":{"row":99,"column":69},"end":{"row":99,"column":70},"action":"insert","lines":["g"]},{"start":{"row":99,"column":70},"end":{"row":99,"column":71},"action":"insert","lines":["h"]},{"start":{"row":99,"column":71},"end":{"row":99,"column":72},"action":"insert","lines":["t"]}],[{"start":{"row":99,"column":56},"end":{"row":99,"column":72},"action":"remove","lines":[", details.height"],"id":3}],[{"start":{"row":101,"column":50},"end":{"row":102,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":102,"column":0},"end":{"row":102,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":102,"column":8},"end":{"row":102,"column":42},"action":"insert","lines":["self.assertEqual(response, 160.00)"],"id":5}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":50},"action":"remove","lines":["        print(response.context[-1]['object_list'])"],"id":6},{"start":{"row":100,"column":60},"end":{"row":101,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":101,"column":36},"end":{"row":101,"column":37},"action":"remove","lines":["6"],"id":7}],[{"start":{"row":101,"column":36},"end":{"row":101,"column":37},"action":"insert","lines":["8"],"id":8}],[{"start":{"row":82,"column":5},"end":{"row":82,"column":6},"action":"remove","lines":[" "],"id":9},{"start":{"row":82,"column":4},"end":{"row":82,"column":5},"action":"remove","lines":["#"]}],[{"start":{"row":83,"column":4},"end":{"row":83,"column":5},"action":"remove","lines":["#"],"id":10}],[{"start":{"row":82,"column":4},"end":{"row":82,"column":5},"action":"insert","lines":["#"],"id":11}],[{"start":{"row":84,"column":5},"end":{"row":84,"column":6},"action":"remove","lines":["#"],"id":12}],[{"start":{"row":85,"column":6},"end":{"row":85,"column":7},"action":"remove","lines":["#"],"id":13}],[{"start":{"row":86,"column":7},"end":{"row":86,"column":8},"action":"remove","lines":["#"],"id":14}],[{"start":{"row":87,"column":8},"end":{"row":87,"column":9},"action":"remove","lines":["#"],"id":15}],[{"start":{"row":88,"column":0},"end":{"row":103,"column":8},"action":"remove","lines":["","    #def test_bmi_result_page(self):","     #   details = Physical.objects.get(unit_type=\"Metric\")","      #  response = self.client.post(reverse('bmi_result'), details.height)","       # self.assertEqual(response.status_code, 200)","        #self.assertTemplateUsed(response, 'bmi_result.html')","        #self.assertEqual(response, 160.00)","        ","    ","    def test_my_view(self):","        details = Physical.objects.get(unit_type=\"Metric\")","        response = self.client.get(reverse('bmi_result'))","        self.assertTemplateUsed(response, 'bmi_result.html')","        self.assertEqual(response, 180.00)","        ","        "],"id":16}],[{"start":{"row":78,"column":4},"end":{"row":79,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":79,"column":0},"end":{"row":79,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":79,"column":4},"end":{"row":79,"column":30},"action":"insert","lines":["####### View tests #######"],"id":18}],[{"start":{"row":79,"column":12},"end":{"row":79,"column":16},"action":"remove","lines":["View"],"id":19},{"start":{"row":79,"column":12},"end":{"row":79,"column":13},"action":"insert","lines":["F"]},{"start":{"row":79,"column":13},"end":{"row":79,"column":14},"action":"insert","lines":["o"]},{"start":{"row":79,"column":14},"end":{"row":79,"column":15},"action":"insert","lines":["r"]},{"start":{"row":79,"column":15},"end":{"row":79,"column":16},"action":"insert","lines":["m"]}],[{"start":{"row":78,"column":4},"end":{"row":79,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":79,"column":0},"end":{"row":79,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":81,"column":8},"end":{"row":82,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":82,"column":0},"end":{"row":82,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":17},"action":"remove","lines":["Model Tests"],"id":22},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["T"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["e"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["s"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["t"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["i"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["n"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["g"]}],[{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["#"],"id":23},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["#"]},{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["#"]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["#"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["#"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["#"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["#"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["#"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["#"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["#"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["#"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["#"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["#"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["#"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["#"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["#"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["#"]}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["#"],"id":24},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["#"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["#"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["#"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["#"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["#"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["#"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["#"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["#"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["#"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["#"]},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"insert","lines":["#"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":["#"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":25}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["#"],"id":26},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["I"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["m"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["p"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["o"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["r"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":[" "],"id":27},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["l"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["i"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["b"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["r"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["a"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["r"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["i"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["e"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":[" "],"id":28},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["v"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["i"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["e"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["w"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":[","],"id":29}],[{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":[" "],"id":30},{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":["m"]},{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"insert","lines":["o"]},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["d"]},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["e"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["l"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":[" "],"id":31},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"insert","lines":["a"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":["b"]},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"insert","lines":["d"]}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":[" "],"id":32}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"remove","lines":[" "],"id":33},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"remove","lines":["d"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"remove","lines":["b"]}],[{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":["n"],"id":34},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"insert","lines":["d"]}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":[" "],"id":35},{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":["f"]},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["o"]},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["r"]},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["m"]},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"remove","lines":["s"],"id":36},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"remove","lines":["m"]},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"remove","lines":["r"]},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"remove","lines":["o"]},{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"remove","lines":["f"]},{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"remove","lines":[" "]},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"remove","lines":["d"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"remove","lines":["n"]},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"remove","lines":["a"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"remove","lines":[" "]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"remove","lines":["s"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"remove","lines":["l"]},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"remove","lines":["e"]},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"remove","lines":["d"]},{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"remove","lines":["o"]},{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"remove","lines":["m"]},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"remove","lines":[" "]}],[{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"remove","lines":[","],"id":37}],[{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":[" "],"id":38},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["a"]},{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":["n"]},{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"insert","lines":["d"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":[" "],"id":39},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["m"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["o"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["d"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":["e"]},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"insert","lines":["l"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":93,"column":1},"end":{"row":93,"column":2},"action":"insert","lines":["#"],"id":40},{"start":{"row":93,"column":2},"end":{"row":93,"column":3},"action":"insert","lines":["#"]},{"start":{"row":93,"column":3},"end":{"row":93,"column":4},"action":"insert","lines":["#"]},{"start":{"row":93,"column":4},"end":{"row":93,"column":5},"action":"insert","lines":["#"]},{"start":{"row":93,"column":5},"end":{"row":93,"column":6},"action":"insert","lines":["#"]},{"start":{"row":93,"column":6},"end":{"row":93,"column":7},"action":"insert","lines":["#"]},{"start":{"row":93,"column":7},"end":{"row":93,"column":8},"action":"insert","lines":["#"]},{"start":{"row":93,"column":8},"end":{"row":93,"column":9},"action":"insert","lines":["#"]},{"start":{"row":93,"column":9},"end":{"row":93,"column":10},"action":"insert","lines":["#"]},{"start":{"row":93,"column":10},"end":{"row":93,"column":11},"action":"insert","lines":["#"]},{"start":{"row":93,"column":11},"end":{"row":93,"column":12},"action":"insert","lines":["#"]},{"start":{"row":93,"column":12},"end":{"row":93,"column":13},"action":"insert","lines":["#"]},{"start":{"row":93,"column":13},"end":{"row":93,"column":14},"action":"insert","lines":["#"]},{"start":{"row":93,"column":14},"end":{"row":93,"column":15},"action":"insert","lines":["#"]},{"start":{"row":93,"column":15},"end":{"row":93,"column":16},"action":"insert","lines":["#"]},{"start":{"row":93,"column":16},"end":{"row":93,"column":17},"action":"insert","lines":["#"]},{"start":{"row":93,"column":17},"end":{"row":93,"column":18},"action":"insert","lines":["#"]},{"start":{"row":93,"column":18},"end":{"row":93,"column":19},"action":"insert","lines":["#"]},{"start":{"row":93,"column":19},"end":{"row":93,"column":20},"action":"insert","lines":["#"]},{"start":{"row":93,"column":20},"end":{"row":93,"column":21},"action":"insert","lines":["#"]},{"start":{"row":93,"column":21},"end":{"row":93,"column":22},"action":"insert","lines":["#"]},{"start":{"row":93,"column":22},"end":{"row":93,"column":23},"action":"insert","lines":["#"]},{"start":{"row":93,"column":23},"end":{"row":93,"column":24},"action":"insert","lines":["#"]},{"start":{"row":93,"column":24},"end":{"row":93,"column":25},"action":"insert","lines":["#"]},{"start":{"row":93,"column":25},"end":{"row":93,"column":26},"action":"insert","lines":["#"]},{"start":{"row":93,"column":26},"end":{"row":93,"column":27},"action":"insert","lines":["#"]},{"start":{"row":93,"column":27},"end":{"row":93,"column":28},"action":"insert","lines":["#"]},{"start":{"row":93,"column":28},"end":{"row":93,"column":29},"action":"insert","lines":["#"]},{"start":{"row":93,"column":29},"end":{"row":93,"column":30},"action":"insert","lines":["#"]},{"start":{"row":93,"column":30},"end":{"row":93,"column":31},"action":"insert","lines":["#"]}],[{"start":{"row":93,"column":31},"end":{"row":93,"column":32},"action":"insert","lines":["#"],"id":41},{"start":{"row":93,"column":32},"end":{"row":93,"column":33},"action":"insert","lines":["#"]},{"start":{"row":93,"column":33},"end":{"row":93,"column":34},"action":"insert","lines":["#"]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":42}],[{"start":{"row":93,"column":0},"end":{"row":94,"column":0},"action":"insert","lines":["",""],"id":43}],[{"start":{"row":92,"column":60},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":44},{"start":{"row":93,"column":0},"end":{"row":93,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":93,"column":8},"end":{"row":94,"column":69},"action":"insert","lines":["        self.assertEqual(response.status_code, HTTPStatus.OK)","        self.assertContains(response, \"<h1>Add Book</h1>\", html=True)"],"id":45}],[{"start":{"row":93,"column":12},"end":{"row":93,"column":16},"action":"remove","lines":["    "],"id":46},{"start":{"row":93,"column":8},"end":{"row":93,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":92,"column":60},"end":{"row":93,"column":61},"action":"remove","lines":["","        self.assertEqual(response.status_code, HTTPStatus.OK)"],"id":47}],[{"start":{"row":93,"column":39},"end":{"row":93,"column":56},"action":"remove","lines":["<h1>Add Book</h1>"],"id":48},{"start":{"row":93,"column":39},"end":{"row":93,"column":59},"action":"insert","lines":["<h5>BMI results</h5>"]}],[{"start":{"row":92,"column":60},"end":{"row":93,"column":72},"action":"remove","lines":["","        self.assertContains(response, \"<h5>BMI results</h5>\", html=True)"],"id":49}],[{"start":{"row":92,"column":60},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":50},{"start":{"row":93,"column":0},"end":{"row":93,"column":8},"action":"insert","lines":["        "]},{"start":{"row":93,"column":8},"end":{"row":94,"column":0},"action":"insert","lines":["",""]},{"start":{"row":94,"column":0},"end":{"row":94,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":94,"column":4},"end":{"row":94,"column":8},"action":"remove","lines":["    "],"id":51}],[{"start":{"row":94,"column":4},"end":{"row":98,"column":69},"action":"insert","lines":[" def test_get(self):","        response = self.client.get(\"/books/add/\")","","        self.assertEqual(response.status_code, HTTPStatus.OK)","        self.assertContains(response, \"<h1>Add Book</h1>\", html=True)"],"id":52}],[{"start":{"row":94,"column":4},"end":{"row":94,"column":5},"action":"remove","lines":[" "],"id":53}],[{"start":{"row":95,"column":35},"end":{"row":95,"column":48},"action":"remove","lines":["\"/books/add/\""],"id":57},{"start":{"row":95,"column":35},"end":{"row":95,"column":36},"action":"insert","lines":["'"]},{"start":{"row":95,"column":36},"end":{"row":95,"column":37},"action":"insert","lines":["'"]}],[{"start":{"row":95,"column":36},"end":{"row":95,"column":44},"action":"insert","lines":["bmi_form"],"id":58}],[{"start":{"row":95,"column":46},"end":{"row":96,"column":0},"action":"remove","lines":["",""],"id":59}],[{"start":{"row":96,"column":47},"end":{"row":96,"column":60},"action":"remove","lines":["HTTPStatus.OK"],"id":60},{"start":{"row":96,"column":47},"end":{"row":96,"column":48},"action":"insert","lines":["2"]},{"start":{"row":96,"column":48},"end":{"row":96,"column":49},"action":"insert","lines":["0"]},{"start":{"row":96,"column":49},"end":{"row":96,"column":50},"action":"insert","lines":["0"]}],[{"start":{"row":97,"column":39},"end":{"row":97,"column":56},"action":"remove","lines":["<h1>Add Book</h1>"],"id":61},{"start":{"row":97,"column":39},"end":{"row":97,"column":62},"action":"insert","lines":["<h5>BMI calculator</h5>"]}],[{"start":{"row":95,"column":35},"end":{"row":95,"column":36},"action":"insert","lines":["r"],"id":62},{"start":{"row":95,"column":36},"end":{"row":95,"column":37},"action":"insert","lines":["e"]},{"start":{"row":95,"column":37},"end":{"row":95,"column":38},"action":"insert","lines":["v"]},{"start":{"row":95,"column":38},"end":{"row":95,"column":39},"action":"insert","lines":["e"]},{"start":{"row":95,"column":39},"end":{"row":95,"column":40},"action":"insert","lines":["r"]},{"start":{"row":95,"column":40},"end":{"row":95,"column":41},"action":"insert","lines":["s"]},{"start":{"row":95,"column":41},"end":{"row":95,"column":42},"action":"insert","lines":["e"]},{"start":{"row":95,"column":42},"end":{"row":95,"column":43},"action":"insert","lines":["("]}],[{"start":{"row":95,"column":54},"end":{"row":95,"column":55},"action":"insert","lines":[")"],"id":63}],[{"start":{"row":95,"column":35},"end":{"row":95,"column":54},"action":"remove","lines":["reverse('bmi_form')"],"id":64},{"start":{"row":95,"column":35},"end":{"row":95,"column":44},"action":"insert","lines":["physical/"]}],[{"start":{"row":95,"column":35},"end":{"row":95,"column":36},"action":"insert","lines":["/"],"id":65}],[{"start":{"row":95,"column":35},"end":{"row":95,"column":36},"action":"insert","lines":["'"],"id":66}],[{"start":{"row":95,"column":46},"end":{"row":95,"column":47},"action":"insert","lines":["'"],"id":67}],[{"start":{"row":93,"column":0},"end":{"row":97,"column":75},"action":"remove","lines":["        ","    def test_get(self):","        response = self.client.get('/physical/')","        self.assertEqual(response.status_code, 200)","        self.assertContains(response, \"<h5>BMI calculator</h5>\", html=True)"],"id":68},{"start":{"row":92,"column":60},"end":{"row":93,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":80,"column":0},"end":{"row":85,"column":30},"action":"remove","lines":["    ","    ","    ####### Form tests #######    ","        ","        ","    ####### View tests #######"],"id":69},{"start":{"row":79,"column":61},"end":{"row":80,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":32},"action":"remove","lines":["############################ "],"id":70},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":30,"column":0},"end":{"row":31,"column":31},"action":"remove","lines":["    ","    ####### Model tests #######"],"id":71},{"start":{"row":29,"column":13},"end":{"row":30,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":87,"column":3},"end":{"row":87,"column":34},"action":"remove","lines":["###############################"],"id":72}],[{"start":{"row":219,"column":0},"end":{"row":219,"column":4},"action":"insert","lines":["    "],"id":73}],[{"start":{"row":219,"column":4},"end":{"row":224,"column":60},"action":"insert","lines":["    #Test bmi results page rendered","    def test_bmi_result_page(self):","        url = reverse('bmi_result')","        response = self.client.get(url)","        self.assertEqual(response.status_code, 200)","        self.assertTemplateUsed(response, 'bmi_result.html')"],"id":74}],[{"start":{"row":219,"column":4},"end":{"row":219,"column":8},"action":"remove","lines":["    "],"id":75}],[{"start":{"row":219,"column":10},"end":{"row":219,"column":13},"action":"remove","lines":["bmi"],"id":76},{"start":{"row":219,"column":10},"end":{"row":219,"column":11},"action":"insert","lines":["m"]},{"start":{"row":219,"column":11},"end":{"row":219,"column":12},"action":"insert","lines":["a"]},{"start":{"row":219,"column":12},"end":{"row":219,"column":13},"action":"insert","lines":["c"]},{"start":{"row":219,"column":13},"end":{"row":219,"column":14},"action":"insert","lines":["r"]},{"start":{"row":219,"column":14},"end":{"row":219,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":221,"column":23},"end":{"row":221,"column":26},"action":"remove","lines":["bmi"],"id":77},{"start":{"row":221,"column":23},"end":{"row":221,"column":24},"action":"insert","lines":["m"]},{"start":{"row":221,"column":24},"end":{"row":221,"column":25},"action":"insert","lines":["a"]},{"start":{"row":221,"column":25},"end":{"row":221,"column":26},"action":"insert","lines":["c"]},{"start":{"row":221,"column":26},"end":{"row":221,"column":27},"action":"insert","lines":["r"]},{"start":{"row":221,"column":27},"end":{"row":221,"column":28},"action":"insert","lines":["o"]}],[{"start":{"row":224,"column":43},"end":{"row":224,"column":46},"action":"remove","lines":["bmi"],"id":78},{"start":{"row":224,"column":43},"end":{"row":224,"column":44},"action":"insert","lines":["m"]},{"start":{"row":224,"column":44},"end":{"row":224,"column":45},"action":"insert","lines":["a"]},{"start":{"row":224,"column":45},"end":{"row":224,"column":46},"action":"insert","lines":["c"]},{"start":{"row":224,"column":46},"end":{"row":224,"column":47},"action":"insert","lines":["r"]},{"start":{"row":224,"column":47},"end":{"row":224,"column":48},"action":"insert","lines":["o"]}]]},"ace":{"folds":[],"scrolltop":204,"scrollleft":0,"selection":{"start":{"row":13,"column":30},"end":{"row":13,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1598361606517,"hash":"aacbdf84759ce7afe8f1c2b0681374cecf7b10fd"}