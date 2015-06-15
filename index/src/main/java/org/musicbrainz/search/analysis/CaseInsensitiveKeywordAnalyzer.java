package org.musicbrainz.search.analysis;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.Tokenizer;
import org.apache.lucene.analysis.core.KeywordTokenizer;


/**
 * Keeps input as simple token but always converts to lowercase, to allow searching user uppercase or lowercase
 * queries
 */
public class CaseInsensitiveKeywordAnalyzer extends Analyzer {

    public CaseInsensitiveKeywordAnalyzer() {

    }

    @Override
    protected TokenStreamComponents createComponents(String fieldName) {
        Tokenizer source = new KeywordTokenizer();
        TokenStream filter = new LowercaseFilter(source);
        return new TokenStreamComponents(source, filter);
    }

}

