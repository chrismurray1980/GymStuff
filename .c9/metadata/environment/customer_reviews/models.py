{"filter":false,"title":"models.py","tooltip":"/customer_reviews/models.py","undoManager":{"mark":47,"position":47,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":18,"column":5},"action":"insert","lines":["class Wine(models.Model):","    name = models.CharField(max_length=200)","    ","    def average_rating(self):","        all_ratings = map(lambda x: x.rating, self.review_set.all())","        return np.mean(all_ratings)","        ","    def __unicode__(self):","        return self.name","","","class Review(models.Model):","    RATING_CHOICES = (","        (1, '1'),","        (2, '2'),","        (3, '3'),","        (4, '4'),","        (5, '5'),","    )"]}],[{"start":{"row":18,"column":5},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":24,"column":56},"action":"insert","lines":["    wine = models.ForeignKey(Wine)","    pub_date = models.DateTimeField('date published')","    user_name = models.CharField(max_length=100)","    comment = models.CharField(max_length=200)","    rating = models.IntegerField(choices=RATING_CHOICES)"],"id":4}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["from django.db import models","import numpy as np",""],"id":6}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "],"id":8},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":10,"column":26},"action":"insert","lines":["class Review(models.Model):","    product = models.ForeignKey(Product, on_delete=models.CASCADE)","    user = models.ForeignKey(User, on_delete=models.CASCADE)","    review = models.TextField()","    date = models.DateTimeField(auto_now_add=True)","","    def __str__(self):","        return self.review"],"id":10}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":8,"column":55},"action":"insert","lines":["","from django.contrib.contenttypes.models import ContentType","from django.contrib.contenttypes import generic","from django.contrib.auth.models import User","from django.db import models","from django.utils.translation import ugettext_lazy as _"],"id":12}],[{"start":{"row":4,"column":47},"end":{"row":4,"column":58},"action":"remove","lines":["ContentType"],"id":13},{"start":{"row":4,"column":47},"end":{"row":4,"column":48},"action":"insert","lines":["P"]},{"start":{"row":4,"column":48},"end":{"row":4,"column":49},"action":"insert","lines":["r"]},{"start":{"row":4,"column":49},"end":{"row":4,"column":50},"action":"insert","lines":["o"]},{"start":{"row":4,"column":50},"end":{"row":4,"column":51},"action":"insert","lines":["d"]},{"start":{"row":4,"column":51},"end":{"row":4,"column":52},"action":"insert","lines":["u"]},{"start":{"row":4,"column":52},"end":{"row":4,"column":53},"action":"insert","lines":["c"]},{"start":{"row":4,"column":53},"end":{"row":4,"column":54},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":54},"action":"remove","lines":["","from django.contrib.contenttypes.models import Product"],"id":15}],[{"start":{"row":2,"column":0},"end":{"row":7,"column":55},"action":"remove","lines":["","","from django.contrib.contenttypes import generic","from django.contrib.auth.models import User","from django.db import models","from django.utils.translation import ugettext_lazy as _"],"id":16}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":17},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":18},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"],"id":19},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":20}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["p"],"id":21},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["r"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["o"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["d"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["u"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["c"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["t"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["."],"id":22},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["m"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["o"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["d"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["e"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["l"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":[" "],"id":23},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["i"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["m"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["p"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["r"],"id":24},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":[" "],"id":25}],[{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["P"],"id":26},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["r"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["o"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["d"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["u"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["c"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":60},"action":"remove","lines":["models.ForeignKey(User, on_delete=models.CASCADE)"],"id":27},{"start":{"row":7,"column":11},"end":{"row":7,"column":43},"action":"insert","lines":["models.CharField(max_length=200)"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["/"],"id":28},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["-"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["0"]}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"remove","lines":["0"],"id":29},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"remove","lines":["-"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["/"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["_"],"id":30},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["n"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["a"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["m"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["_"],"id":33}],[{"start":{"row":8,"column":31},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":52},"action":"insert","lines":["","rating = models.IntegerField(choices=RATING_CHOICES)"],"id":35}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"remove","lines":["",""],"id":36}],[{"start":{"row":5,"column":27},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["    RATING_CHOICES = (","        (1, '1'),","        (2, '2'),","        (3, '3'),","        (4, '4'),","        (5, '5'),","    )"],"id":38}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":39},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":21,"column":0},"end":{"row":49,"column":52},"action":"remove","lines":["","","","","class Wine(models.Model):","    name = models.CharField(max_length=200)","    ","    def average_rating(self):","        all_ratings = map(lambda x: x.rating, self.review_set.all())","        return np.mean(all_ratings)","        ","    def __unicode__(self):","        return self.name","","","class Review(models.Model):","    RATING_CHOICES = (","        (1, '1'),","        (2, '2'),","        (3, '3'),","        (4, '4'),","        (5, '5'),","    )","    ","wine = models.ForeignKey(Wine)","pub_date = models.DateTimeField('date published')","user_name = models.CharField(max_length=100)","comment = models.CharField(max_length=200)","rating = models.IntegerField(choices=RATING_CHOICES)"],"id":40},{"start":{"row":20,"column":26},"end":{"row":21,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["R"],"id":41},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["c"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["u"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["s"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["t"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["o"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["m"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["e"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["_"],"id":42},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":18},"action":"remove","lines":["import numpy as np"],"id":43},{"start":{"row":0,"column":28},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"insert","lines":["."],"id":44},{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"insert","lines":["i"]},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":["d"]}],[{"start":{"row":12,"column":39},"end":{"row":12,"column":42},"action":"remove","lines":[".id"],"id":45}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":31},"action":"remove","lines":["models.TextField()"],"id":46},{"start":{"row":14,"column":13},"end":{"row":14,"column":45},"action":"insert","lines":["models.CharField(max_length=200)"]}],[{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"remove","lines":["2"],"id":47},{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"insert","lines":["6"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":10},"action":"remove","lines":["review"],"id":48},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["c"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["o"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["m"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["m"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["e"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["n"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":20},"end":{"row":19,"column":26},"action":"remove","lines":["review"],"id":49},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["c"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["o"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["m"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["m"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["e"]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["n"]},{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["r"],"id":50},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["a"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":["h"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"remove","lines":["C"]}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["T"],"id":51},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["e"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["x"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":31},"end":{"row":14,"column":45},"action":"remove","lines":["max_length=600"],"id":52}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":31},"end":{"row":14,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1595754918616,"hash":"7c8bd0551d059a2daf0792ebc8911868691bd966"}