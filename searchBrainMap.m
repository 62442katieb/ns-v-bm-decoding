clear all

% Search BrainMap data dump
file = '/home/data/nbc/athena/JournalInfo_athena.mat';

LV = load(file);

AllExperiments = LV.Experiments;

searchTerms = {'Emotion.Anger', 'Emotion.Sadness'};
for iTerm = 1:length(searchTerms)
    termName = strsplit(searchTerms{iTerm}, '.');
    termName = termName{end};
    
    c = 1;
    for jExp = 1:length(AllExperiments)
        % First pass
        if strcmp(AllExperiments(jExp).Type, 'Activations') && isequal(AllExperiments(jExp).Diagnosis, {'Normals'})
            if any(ismember(AllExperiments(jExp).BD, searchTerms{iTerm}))
                Experiments(c) = AllExperiments(jExp);
                c = c + 1;
            end
        end
    end
    save(strcat('/home/data/nbc/tools/gingerale/refactoredALE/DataMatlab/', 'museum_', termName, '.mat'), 'Experiments');
    clear Experiments
end
