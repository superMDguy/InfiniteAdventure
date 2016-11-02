from random import choice
from nltk.corpus import wordnet as wn

def form(syn):
	hyps = []
	for hyp in wn.synset(syn).hyponyms():
		for name in hyp.lemma_names():
			hyps.append(name.replace('_', ' '))
		for hyp2 in hyp.hyponyms():
			for name in hyp.lemma_names():
				hyps.append(name.replace('_', ' '))
	return choice(hyps)

def similar(word):
	sims = []
	for ss in wn.synsets(word):
		for sim in ss.similar_tos():
			for lemma in sim.lemma_names():
				sims.append(lemma.replace('_', ' '))
		for ss2 in wn.synsets(ss.name()):
			for sim2 in ss2.similar_tos():
				for lemma in sim2.lemma_names():
					sims.append(lemma.replace('_', ' '))

	return choice(sims)

def randomBuilding():
	directions = ['Up ahead', 'In front of you', 'A few steps away', 'Far off']
	phrases = ["You feel like you should check it out.", "You wonder what's inside.", "You consider going in.", "You feel drawn to go inside it."]
	return "{0}, you see a(n) {1} {2} {3}.  {4}".format(choice(directions), similar('interesting'), similar('chromatic'), form('dwelling.n.01'), choice(phrases))


print(randomBuilding())
print(similar('interesting'))
