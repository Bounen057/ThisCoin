


# Mention から ID

def MentionToID(self, mention){
    mention = mention.replace('<','')
    mention = mention.replace('>','')
    mention = mention.replace('!','')
    mention = mention.replace('@','')

    return mention
}